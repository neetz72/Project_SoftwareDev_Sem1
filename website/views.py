#contains the url endpoints 

from flask import Blueprint, render_template, request, flash
from .models import Ice
from . import db



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
        variance = target - actual #calculate the variance and display to front-end

        #Error Handling

      #  station_id = db.Column(db.String(20), primary_key=True, unique=True)
    #target = db.Column(db.Numeric) #float
   # actual = db.Column(db.Numeric)
    #variance = db.Column(db.Numeric)
    #date = db.Column(db.String(20)) #data type date   
        if int(actual) > 1000:
            flash('Actual value cannot be greater then 1000', category='Error')
        else: 
            #new_entry = Ice(date=date,target=target,actual=actual,variance = variance)

            stn = Ice.query.filter_by(station_id = stationId)
            if stn: 
                new_entry = Ice(date=date,actual=actual)
                tar = Ice.query.filter_by(station_id = stationId)

            db.session.add(new_entry) #will add new entry to the DB 
            db.session.commit() #we ask the db to commit the changes made to the db and update itself
            flash('Thank you for updating the Ice cream concentration, have a good fucking day.', category='success')

        



    return render_template("app.html")
    
@views.route('/developers')
def developers():
    return render_template("developers.html")

@views.route('/station', methods=['GET', 'POST'])
def station():


    if request.method == 'POST':
        station_id = request.form.get('stationId')#should be displayed in the frontend after getting queried from the db
        target = request.form.get('target')#should be queried from DB for the selected station 
      

        #Error Handling

      #  station_id = db.Column(db.String(20), primary_key=True, unique=True)
    #target = db.Column(db.Numeric) #float
   # actual = db.Column(db.Numeric)
    #variance = db.Column(db.Numeric)
    #date = db.Column(db.String(20)) #data type date   
        if station_id == None:
            flash('Enter station ID', category='Error')
        else: 
            new_entry = Ice(station_id=station_id,target=target)
            db.session.add(new_entry) #will add new entry to the DB 
            db.session.commit() #we ask the db to commit the changes made to the db and update itself
            flash('Thank you for adding a new station', category='success')


    return render_template("station.html")
