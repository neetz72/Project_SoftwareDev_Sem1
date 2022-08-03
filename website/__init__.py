#will make the website folder into a pyhton package

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path

#initialize a new data base 
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app(): #the function that creates an app and initializes it with a secret key for encryption 
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'nasknfkasbngdoasogdasndg'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	#initialize the db with our app
	db.init_app(app)

	#lets register the blueprints 

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix = '/')
	app.register_blueprint(auth, url_prefix = '/')

	from .models import Ice

	if path.exists('website/' + DB_NAME):
		print("DB already exists~!")
	else:
		db.create_all(app=app)
		print('~DB CREATED~!!!')
	
	return app 



	


	

	 