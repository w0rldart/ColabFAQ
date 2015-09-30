from flask import request

# from flask.ext.security.forms import ConfirmRegisterForm
from flask_security.forms import LoginForm, RegisterForm
# from flask.ext.security.utils import verify_and_update_password

# from flask.ext.wtf.html5 import EmailField

from wtforms import StringField, PasswordField
from wtforms.validators import required, email, optional

errors = {
    'required': {
        'email': 'Email address is required',
        'first_name': 'First name is required',
        'last_name': 'Last name is required',
        'password': 'Password is required',
    },
    'password_confirm': 'Passwords must match'
}

class ExtendedLoginForm(LoginForm):
    email = StringField(None, description="Email address")
    password = PasswordField(None, description="Password")
    # remember = BooleanField(get_form_field_label('remember_me'))
    # submit = SubmitField(get_form_field_label('login'))

class ExtendedRegisterForm(RegisterForm):
    email            = StringField(None, validators=[required(message=errors['required']['email'])], description="Email address")
    first_name       = StringField(None, validators=[required(message=errors['required']['first_name'])], description="First name")
    last_name        = StringField(None, validators=[required(message=errors['required']['last_name'])], description="Last name")
    password         = PasswordField(None, validators=[required(message=errors['required']['password'])], description="Choose a password")
    password_confirm = PasswordField(None, validators=[required(message=errors['password_confirm'])], description="Confirm your password")