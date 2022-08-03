#contains the url endpoints 

from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) #whenever we navigate to this URL what ever is the home function below will run
def home():
    #data = request.form #contains all of the data that was sent as part of our form
    #print(data)

    if request.method == 'POST':
        stationId = request.form.get('stationId')#should be displayed in the frontend after getting queried from the db
        date = request.form.get('date')#selected by user
        target = request.form.get('target')#should be queried from DB for the selected station 
        actual = request.form.get('actual') #entered by the user
        variance = request.form.get('variance') #calculate the variance and display to front-end

        #Error Handling
        if int(actual) > 1000:
            flash('Actual value cannot be greater then 1000', category='Error')
        else: 
            flash('Thank you for updating the Ice cream concentration, have a good fucking day.', category='success')

        



    return render_template("app.html")
    
@views.route('/developers')
def developers():
    return render_template("developers.html")