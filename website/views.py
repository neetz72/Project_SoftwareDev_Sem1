#contains the url endpoints 

from flask import Blueprint, render_template 

views = Blueprint('views', __name__)

@views.route('/') #whenever we navigate to this URL what ever is the home function below will run
def home():
    return render_template("app.html")
    
@views.route('/developers')
def developers():
    return render_template("developers.html")