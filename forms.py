from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField, FloatField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin', 'Admin'), ('headmaster', 'Headmaster'), ('teacher', 'Teacher'), ('student', 'Student'), ('parent', 'Parent')], validators=[DataRequired()])
    teacher_type = SelectField('Teacher Type', choices=[('', 'None'), ('class_teacher', 'Class Teacher'), ('subject_teacher', 'Subject Teacher'), ('librarian', 'Librarian'), ('accountant', 'Accountant')], validators=[Optional()])
    submit = SubmitField('Register')

class InstituteForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    logo = StringField('Logo URL', validators=[Optional()])
    tagline = StringField('Tagline', validators=[Optional()])
    schema = StringField('Schema', validators=[DataRequired()])
    submit = SubmitField('Save')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=[('admin', 'Admin'), ('headmaster', 'Headmaster'), ('teacher', 'Teacher'), ('student', 'Student'), ('parent', 'Parent')])
    teacher_type = SelectField('Teacher Type', choices=[('', 'None'), ('class_teacher', 'Class Teacher'), ('subject_teacher', 'Subject Teacher'), ('librarian', 'Librarian'), ('accountant', 'Accountant')])
    submit = SubmitField('Save')

class PermissionForm(FlaskForm):
    feature = StringField('Feature', validators=[DataRequired()])
    enabled = SelectField('Enabled', choices=[('True', 'Yes'), ('False', 'No')])
    submit = SubmitField('Save')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    class_id = IntegerField('Class ID', validators=[DataRequired()])
    submit = SubmitField('Save')

class AttendanceForm(FlaskForm):
    student_id = IntegerField('Student ID', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')], validators=[DataRequired()])
    submit = SubmitField('Save')

class ExamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Save')

class GradeForm(FlaskForm):
    student_id = IntegerField('Student ID', validators=[DataRequired()])
    exam_id = IntegerField('Exam ID', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    marks = IntegerField('Marks', validators=[DataRequired()])
    submit = SubmitField('Save')

class TimetableForm(FlaskForm):
    class_id = IntegerField('Class ID', validators=[DataRequired()])
    day = StringField('Day', validators=[DataRequired()])
    period = IntegerField('Period', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    teacher_id = IntegerField('Teacher ID', validators=[DataRequired()])
    submit = SubmitField('Save')

class FeeForm(FlaskForm):
    student_id = IntegerField('Student ID', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    submit = SubmitField('Save')

class PayrollForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Save')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[Optional()])
    submit = SubmitField('Save')

class InventoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Save')

class TransportForm(FlaskForm):
    name = StringField('Route Name', validators=[DataRequired()])
    vehicle_id = StringField('Vehicle ID', validators=[DataRequired()])
    submit = SubmitField('Save')

class HostelForm(FlaskForm):
    room_number = StringField('Room Number', validators=[DataRequired()])
    student_id = IntegerField('Student ID', validators=[Optional()])
    submit = SubmitField('Save')

class NotificationForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    recipient_id = IntegerField('Recipient ID', validators=[Optional()])
    submit = SubmitField('Send')

class PaymentForm(FlaskForm):
    payment_method = SelectField('Payment Method', choices=[('qr', 'QR Code'), ('paypal', 'PayPal'), ('stripe', 'Stripe')], validators=[DataRequired()])
    submit = SubmitField('Proceed')