from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, EmailField, PasswordField, Form, validators, ValidationError
from wtforms.validators import DataRequired
from flask_wtf import Form
from .models import User


class UserForm(FlaskForm):

    username = StringField('username', name='username', )
    email = EmailField('email',name='email')
    password = PasswordField('password',  name='password')
     
    def validate_username(self, username):
        if not username.data.strip():
            raise ValidationError('Please enter a username ')
        else:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('Username is already taken. Please choose a different one.')

    def validate_email(self, email):
        
        if not email.data.strip():
            raise ValidationError("please enter a email ")
        else:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email is already registered. Please use a different email.')
            
    
    def validate_password(self, password):
        if not password.data.strip():
            raise ValidationError("please enter a Password ")
        else:
            if User.query.filter_by(password=hash(password.data)).first():
                raise ValidationError('Email is already registered. Please use a different email.')
    
    
    class Meta:
        model = User
