__version__ = "0.1"
from flask import Flask

app = Flask('app')
app.config['SECRET_KEY'] = 'random'

app = Flask(__name__, template_folder="views")

app.debug = True

from app.routes.home_router import home_router
app.register_blueprint(home_router)
