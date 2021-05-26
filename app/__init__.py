__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask('app')

app = Flask(__name__, template_folder="views")

#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbmipropy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

from app.routes.principal_router import principal_router
app.register_blueprint(principal_router)

from app.routes.home_router import home_router
app.register_blueprint(home_router)

from app.routes.alumno_router import alumno_router
app.register_blueprint(alumno_router)
