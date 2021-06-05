__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import secrets

UPLOAD_FOLDER = 'app/static/uploads/'
#app = Flask('app')

app = Flask(__name__, template_folder="views")

#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbmipropy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)

from app.routes.principal_router import principal_router
app.register_blueprint(principal_router)

from app.routes.home_router import home_router
app.register_blueprint(home_router)

from app.routes.alumno_router import alumno_router
app.register_blueprint(alumno_router)

from app.routes.materia_router import materia_router
app.register_blueprint(materia_router)

from app.routes.practica_router import practica_router
app.register_blueprint(practica_router)

from app.routes.carrusel_router import carrusel_router
app.register_blueprint(carrusel_router)