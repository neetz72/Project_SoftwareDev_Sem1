
#THIS IS THE CONTROLLER

from statistics import variance
from flask import Blueprint, render_template, request, flash
from .models import Ice
from . import db



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) #whenever we navigate to this URL what ever is the home function below will run
def home():
    #data = request.form #contains all of the data that was sent as part of our form
    #print(data)
    station_data = Ice.query.all()
    for station in station_data:
        print (station.station_id)
        print (station.variance)

    if request.method == 'POST':
        stationId = request.form.get('stationId')#should be displayed in the frontend after getting queried from the db
        date = request.form.get('date')#selected by user
        #target = request.form.get('target')#should be queried from DB for the selected station 
        actual = request.form.get('actual') #entered by the user
      #  variance = target - actual #calculate the variance and display to front-end

        #Error Handling

      #  station_id = db.Column(db.String(20), primary_key=True, unique=True)
    #target = db.Column(db.Numeric) #float
   # actual = db.Column(db.Numeric)
    #variance = db.Column(db.Numeric)
    #date = db.Column(db.String(20)) #data type date   
        if int(actual) > 1000:
            #FUTURE SCOPE
            # station_data = Ice.query.all()
            # delete_this = station_data
            # db.session.delete(delete_this)
            # db.session.commit()
            flash('You have deleted your database : CONGRATULATIONS !', category='Error')

        else: 
            #new_entry = Ice(date=date,target=target,actual=actual,variance = variance)

            #The system then calculates and displays the variance from the target. The system
            #highlights the variance in red when it is 10% or more below the target, or in green
            #when 5% or more above the target.

            stn = Ice.query.filter_by(station_id = stationId).first()
            if stn: 
                stn.date = date
                stn.actual = float(actual)
                db.session.commit()
                #tar = Ice.query.filter_by(station_id = stationId).target
                tar = float(stn.target)
                ac = float (actual)
                variance =   ac - tar

                ten = tar * 0.10
                five = tar *0.05

                tarAboveFive = tar + five

                tarTenBelow = tar- ten

                if ac < tarTenBelow:
                    flash(f'The Variance is below the threshold of 10% {variance}', category='error')
                elif ac > tarAboveFive:
                    flash(f'The Variance is above the threshold of 5% {variance}', category='success')
                else:
                    flash(f'The Variance is in between the threshold {variance}', category='success')





                stn.variance = float(variance)
                db.session.commit()



            #db.session.add(new_entry) #will add new entry to the DB 
            #db.session.commit() #we ask the db to commit the changes made to the db and update itself
            # if int(variance) > 0 : 
            #     flash(f'The Variance is positive {variance}', category='success')
            # else: 
            #     flash(f'The Variance is negative {variance}', category='error')

            

        



    return render_template("app2.html", stndata=station_data)
    
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
            flash('Enter station ID', category='error')
        else: 
            stn = Ice.query.filter_by(station_id = station_id).first()
            if stn:
                flash('Station already Exists!', category = 'error')
            else:
                new_entry = Ice(station_id=station_id,target=target)
                db.session.add(new_entry) #will add new entry to the DB 
                db.session.commit() #we ask the db to commit the changes made to the db and update itself
                flash('Thank you for adding a new station', category='success')

            


    return render_template("station2.html")
