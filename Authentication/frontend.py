from flask import Blueprint, render_template, flash, request, redirect, url_for
from .forms import UserForm
from .models import User
from .models import db

front_bp = Blueprint('fe' , __name__, url_prefix='/')


@front_bp.route('/signup', methods = ['POST', 'GET'])
def register_frontend():
    
    form = UserForm()
    
    try:
        error = None
        if request.method == 'POST' and form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username=username, email=email, password=hash(password))
            db.session.add(user)
            execute = db.session.commit()
           
            flash(message=f"Welcome {username} Thanks for registering", )
            form= UserForm(formdata=None)
            return redirect(url_for('signup'))

    except Exception as e:
        print("Exception occutred" ,e)



    return render_template('signup.html', form = form)