from flask import Blueprint

auth = Blueprint('views',__name__)

auth.route('/login')
def login():
    return 

