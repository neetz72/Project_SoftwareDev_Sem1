#lets add some authentication 

from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('login')
def login():
    return "<h1>login</h1>"
