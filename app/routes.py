from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/demo/<role>')
def demo(role):
    valid_roles = ['superadmin', 'admin', 'teacher', 'student', 'parent']
    if role not in valid_roles:
        return render_template('index.html', error="Invalid demo role")
    return render_template(f'demo_{role}.html', role=role)