# Navigation for the user 
from flask import Blueprint

views = Blueprint('view,__name__')

# whenever the user goes to the root directory this function is called 
@views.route('/')
def home():
    pass