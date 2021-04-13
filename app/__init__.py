__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SECRET_KEY'] = 'random'

app = Flask(__name__, template_folder="views")

#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbmipropy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

app.debug = True

from app.routes.home_router import home_router
app.register_blueprint(home_router)
