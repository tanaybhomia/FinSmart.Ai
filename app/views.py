from flask import Blueprint
from flask import render_template

view = Blueprint('view', __name__)

@view.route('/')  # Decorator
def home():
    return render_template('dashboard.html')
