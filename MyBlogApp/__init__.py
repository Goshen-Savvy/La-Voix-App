from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#database configuration
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '2684bf26940afb4cbf8de06cce1b5a00'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login' #this handles the account page if I try to access it without logging in first
login_manager.login_message_category='info'

from MyBlogApp import routes