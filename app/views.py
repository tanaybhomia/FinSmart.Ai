# Navigation for the user 
from flask import Blueprint
from flask import render_template

views = Blueprint('view',__name__)
 
@views.route('/') #decorator
def home():
    return render_template('dashboard.html')