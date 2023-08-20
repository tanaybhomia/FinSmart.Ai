from flask import Blueprint
from flask import render_template

view = Blueprint('view', __name__,static_folder='static')

@view.route('/')  # Decorator
def home():
    return render_template('dashboard.html')
