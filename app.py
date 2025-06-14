from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, timedelta
from functools import wraps
from forms import *
from models import *
from config import Config
import os
import requests
import stripe
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
csrf = CSRFProtect(app)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session and not get_jwt_identity():
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            identity = get_jwt_identity()
            user = User.query.filter_by(username=identity).first()
            if user.role not in roles:
                flash('Access denied.', 'error')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def is_demo_mode():
    return session.get('demo_mode', False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            session['user_id'] = user.id
            session['institute_id'] = user.institute_id
            session['role'] = user.role
            session['teacher_type'] = user.teacher_type
            access_token = create_access_token(identity=user.username)
            session['access_token'] = access_token
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.', 'error')
    return render_template('login.html', form=form)

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        institute = Institute.query.filter_by(name='Sample Institute').first()
        if not institute:
            flash('No institute found. Contact admin.', 'error')
            return redirect(url_for('register'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            institute_id=institute.id,
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password,
            role=form.role.data,
            teacher_type=form.teacher_type.data or None
        )
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/auth/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/auth/demo', methods=['GET', 'POST'])
def demo():
    session['demo_mode'] = True
    session['institute_id'] = 1
    session['demo_expiry'] = (datetime.now() + timedelta(minutes=15)).timestamp()
    user = User.query.filter_by(username='superadmin', institute_id=1).first()
    if user:
        session['user_id'] = user.id
        session['role'] = user.role
        session['teacher_type'] = user.teacher_type
        access_token = create_access_token(identity=user.username)
        session['access_token'] = access_token
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
@login_required
@jwt_required()
def dashboard():
    if is_demo_mode() and datetime.now().timestamp() > session.get('demo_expiry', 0):
        session.clear()
        flash('Demo session expired.', 'info')
        return redirect(url_for('index'))
    identity = get_jwt_identity()
    user = User.query.filter_by(username=identity).first()
    return render_template(f'dashboards/{user.role}.html', user=user, is_demo=is_demo_mode())

@app.route('/institute', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('super_admin')
def institute():
    form = InstituteForm()
    if form.validate_on_submit() and not is_demo_mode():
        institute = Institute(
            name=form.name.data,
            logo=form.logo.data,
            tagline=form.tagline.data,
            schema=form.schema.data
        )
        db.session.add(institute)
        db.session.commit()
        flash('Institute created.', 'success')
        return redirect(url_for('institute'))
    institutes = Institute.query.all()
    return render_template('modules/institutes.html', form=form, institutes=institutes, is_demo=is_demo_mode())

@app.route('/users', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster')
def users():
    form = UserForm()
    if form.validate_on_submit() and not is_demo_mode():
        user = User(
            institute_id=session['institute_id'],
            username=form.username.data,
            email=form.email.data,
            password_hash=bcrypt.generate_password_hash('default123').decode('utf-8'),
            role=form.role.data,
            teacher_type=form.teacher_type.data or None
        )
        db.session.add(user)
        db.session.commit()
        flash('User created.', 'success')
        return redirect(url_for('users'))
    users = User.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/users.html', form=form, users=users, is_demo=is_demo_mode())

@app.route('/permissions', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster')
def permissions():
    form = PermissionForm()
    if form.validate_on_submit() and not is_demo_mode():
        permission = Permission(
            institute_id=session['institute_id'],
            feature=form.feature.data,
            enabled=form.enabled.data == 'True'
        )
        db.session.add(permission)
        db.session.commit()
        flash('Permission set.', 'success')
        return redirect(url_for('permissions'))
    permissions = Permission.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/permissions.html', form=form, permissions=permissions, is_demo=is_demo_mode())

@app.route('/academic/students', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def students():
    form = StudentForm()
    if form.validate_on_submit() and not is_demo_mode():
        student = Student(
            institute_id=session['institute_id'],
            user_id=session['user_id'],
            name=form.name.data,
            class_id=form.class_id.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Student added.', 'success')
        return redirect(url_for('students'))
    students = Student.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/students.html', form=form, students=students, is_demo=is_demo_mode())

@app.route('/academic/attendance', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def attendance():
    form = AttendanceForm()
    if form.validate_on_submit() and not is_demo_mode():
        attendance = Attendance(
            institute_id=session['institute_id'],
            student_id=form.student_id.data,
            date=form.date.data,
            status=form.status.data
        )
        db.session.add(attendance)
        db.session.commit()
        flash('Attendance recorded.', 'success')
        return redirect(url_for('attendance'))
    attendance = Attendance.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/attendance.html', form=form, attendance=attendance, is_demo=is_demo_mode())

@app.route('/academic/exams', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def exams():
    form = ExamForm()
    if form.validate_on_submit() and not is_demo_mode():
        exam = Exam(
            institute_id=session['institute_id'],
            name=form.name.data,
            date=form.date.data
        )
        db.session.add(exam)
        db.session.commit()
        flash('Exam created.', 'success')
        return redirect(url_for('exams'))
    exams = Exam.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/exams.html', form=form, exams=exams, is_demo=is_demo_mode())

@app.route('/academic/grades', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def grades():
    form = GradeForm()
    if form.validate_on_submit() and not is_demo_mode():
        grade = Grade(
            institute_id=session['institute_id'],
            student_id=form.student_id.data,
            exam_id=form.exam_id.data,
            subject=form.subject.data,
            marks=form.marks.data
        )
        db.session.add(grade)
        db.session.commit()
        flash('Grade assigned.', 'success')
        return redirect(url_for('grades'))
    grades = Grade.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/grades.html', form=form, grades=grades, is_demo=is_demo_mode())

@app.route('/academic/timetable', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def timetable():
    form = TimetableForm()
    if form.validate_on_submit() and not is_demo_mode():
        timetable = Timetable(
            institute_id=session['institute_id'],
            class_id=form.class_id.data,
            day=form.day.data,
            period=form.period.data,
            subject=form.subject.data,
            teacher_id=form.teacher_id.data
        )
        db.session.add(timetable)
        db.session.commit()
        flash('Timetable updated.', 'success')
        return redirect(url_for('timetable'))
    timetable = Timetable.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/timetable.html', form=form, timetable=timetable, is_demo=is_demo_mode())

@app.route('/finance/fees', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def fees():
    form = FeeForm()
    if form.validate_on_submit() and not is_demo_mode():
        fee = Fee(
            institute_id=session['institute_id'],
            student_id=form.student_id.data,
            amount=form.amount.data,
            due_date=form.due_date.data
        )
        db.session.add(fee)
        db.session.commit()
        flash('Fee recorded.', 'success')
        return redirect(url_for('fees'))
    fees = Fee.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/fees.html', form=form, fees=fees, is_demo=is_demo_mode())

@app.route('/finance/payroll', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def payroll():
    form = PayrollForm()
    if form.validate_on_submit() and not is_demo_mode():
        payroll = Payroll(
            institute_id=session['institute_id'],
            user_id=form.user_id.data,
            amount=form.amount.data,
            date=form.date.data
        )
        db.session.add(payroll)
        db.session.commit()
        flash('Payroll recorded.', 'success')
        return redirect(url_for('payroll'))
    payrolls = Payroll.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/payroll.html', form=form, payrolls=payrolls, is_demo=is_demo_mode())

@app.route('/library/books', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def books():
    form = BookForm()
    if form.validate_on_submit() and not is_demo_mode():
        book = Book(
            institute_id=session['institute_id'],
            title=form.title.data,
            author=form.author.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Book added.', 'success')
        return redirect(url_for('books'))
    books = Book.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/library.html', form=form, books=books, is_demo=is_demo_mode())

@app.route('/inventory/items', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def items():
    form = InventoryForm()
    if form.validate_on_submit() and not is_demo_mode():
        item = InventoryItem(
            institute_id=session['institute_id'],
            name=form.name.data,
            quantity=form.quantity.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Item added.', 'success')
        return redirect(url_for('items'))
    items = InventoryItem.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/inventory.html', form=form, items=items, is_demo=is_demo_mode())

@app.route('/transport/routes', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def routes():
    form = TransportForm()
    if form.validate_on_submit() and not is_demo_mode():
        route = TransportRoute(
            institute_id=session['institute_id'],
            name=form.name.data,
            vehicle_id=form.vehicle_id.data
        )
        db.session.add(route)
        db.session.commit()
        flash('Route added.', 'success')
        return redirect(url_for('routes'))
    routes = TransportRoute.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/transport.html', form=form, routes=routes, is_demo=is_demo_mode())

@app.route('/hostel/rooms', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def rooms():
    form = HostelForm()
    if form.validate_on_submit() and not is_demo_mode():
        room = HostelRoom(
            institute_id=session['institute_id'],
            room_number=form.room_number.data,
            student_id=form.student_id.data or None
        )
        db.session.add(room)
        db.session.commit()
        flash('Room added.', 'success')
        return redirect(url_for('rooms'))
    rooms = HostelRoom.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/hostel.html', form=form, rooms=rooms, is_demo=is_demo_mode())

@app.route('/notification/notifications', methods=['GET', 'POST'])
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher')
def notifications():
    form = NotificationForm()
    if form.validate_on_submit() and not is_demo_mode():
        notification = Notification(
            institute_id=session['institute_id'],
            message=form.message.data,
            recipient_id=form.recipient_id.data or None
        )
        db.session.add(notification)
        db.session.commit()
        flash('Notification sent.', 'success')
        return redirect(url_for('notifications'))
    notifications = Notification.query.filter_by(institute_id=session['institute_id']).all()
    return render_template('modules/notifications.html', form=form, notifications=notifications, is_demo=is_demo_mode())

@app.route('/reports')
@login_required
@jwt_required()
@role_required('admin', 'headmaster', 'teacher', 'student', 'parent')
def reports():
    attendance = Attendance.query.filter_by(institute_id=session['institute_id']).limit(10).all()
    grades = Grade.query.filter_by(institute_id=session['institute_id']).limit(10).all()
    return render_template('modules/reports.html', attendance=attendance, grades=grades, is_demo=is_demo_mode())

@app.route('/payment', methods=['GET', 'POST'])
@login_required
@jwt_required()
def payment():
    form = PaymentForm()
    qr_code = 'images/qr_payment.png'
    if form.validate_on_submit():
        payment_method = form.payment_method.data
        if payment_method == 'qr':
            flash('Scan the QR code to proceed with payment.', 'info')
            return render_template('payment.html', form=form, qr_code=qr_code, message='Scan the QR code.')
        elif payment_method == 'paypal':
            return jsonify({'client_id': PAYPAL_CLIENT_ID, 'url': '/payment/paypal/complete'})
        elif payment_method == 'stripe':
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': 'School Fee'},
                        'unit_amount': 5000,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=url_for('payment_success', _external=True),
                cancel_url=url_for('payment_cancel', _external=True),
            )
            return jsonify({'id': session.id})
    return render_template('payment.html', form=form, qr_code=qr_code)

@app.route('/payment/paypal/complete', methods=['POST'])
@login_required
@jwt_required()
def paypal_complete():
    data = request.json
    # Placeholder: Verify PayPal payment with API
    flash('PayPal payment completed (demo).', 'success')
    return jsonify({'status': 'success'})

@app.route('/payment/success')
@login_required
@jwt_required()
def payment_success():
    flash('Payment successful.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/payment/cancel')
@login_required
@jwt_required()
def payment_cancel():
    flash('Payment cancelled.', 'error')
    return redirect(url_for('payment'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)