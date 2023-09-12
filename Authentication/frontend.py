from flask import Blueprint, render_template
from .forms import UserForm

front_bp = Blueprint('fe' , __name__, url_prefix='/')


@front_bp.route('/signup', methods = ['POST', 'GET'])
def register_frontend():
    form = UserForm()
    return render_template('signup.html', form = form)