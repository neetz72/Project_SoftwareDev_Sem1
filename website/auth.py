#FUTURE SCOPE

from flask import Blueprint

auth = Blueprint('auth', __name__)

#SHA256 encryption 

@auth.route('login')
def login():
    return "<h1>login</h1>"
