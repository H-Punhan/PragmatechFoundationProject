from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db/test.db'
app.config['UPLOAD_FOLDER']='setting/static/img'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)

migrate=Migrate(app,db)

import model
from admin import routes
import user


