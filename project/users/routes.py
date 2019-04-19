from datetime import datetime   #pragma: no cover
from flask import flash, redirect, render_template, request, \
    url_for, Blueprint  #pragma: no cover
from flask_login import login_user, login_required, logout_user #pragma: no cover

from .forms import LoginForm    #pragma: no cover
from project.models import User, bcrypt #pragma: no cover


# Config
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   #pragma: no cover


# routes
@users_blueprint.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(
                username=request.form['username']).first()
            remember_me = form.remember.data
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user, remember=remember_me)
                flash('Login successful', 'success')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error, now=datetime.utcnow())


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))
