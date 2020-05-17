from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database configuration
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '2684bf26940afb4cbf8de06cce1b5a00'
db = SQLAlchemy(app)

from MyBlogApp import routes