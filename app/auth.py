# from flask import Blueprint, render_template, redirect, url_for, request, flash
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# from app.models import User

# auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# login_manager = LoginManager()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))

#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

#         user = User.get(username)
#         if user and user.check_password(password):
#             login_user(user)
#             return redirect(url_for('main.index'))
#         else:
#             flash('Invalid username or password', 'error')

#     return render_template('login.html')

# @auth_bp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))

# @login_manager.unauthorized_handler
# def unauthorized():
#     return redirect(url_for('auth.login'))
