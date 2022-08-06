#contains database models 

from . import db
#for the purpose of logging in users (if necessary)
from flask_login import UserMixin
from sqlalchemy.sql import func

#class Target(db.Model):
 #   station_id = db.Column(db.String(20), primary_key=True, unique=True)
  #  target = db.Column(db.Numeric)
   # created_date = db.Column(db.DateTime(timezone=True), default=func.now())
class Ice(db.Model):
    station_id = db.Column(db.String(20), primary_key=True, unique=True)
    target = db.Column(db.Integer) #float
    actual = db.Column(db.Integer)
    variance = db.Column(db.Integer)
    date = db.Column(db.String(20)) #data type date   
