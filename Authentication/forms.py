from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import Form
from .models import User


class UserForm(FlaskForm):

    username = StringField('username', name='username')
    email = EmailField('email',name='email')
    password = PasswordField('password', name='password')
     

    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password = password

    class Meta:
        model = User
