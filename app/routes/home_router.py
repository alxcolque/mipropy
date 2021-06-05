from flask import Blueprint
from app.controllers.HomeController import homecontroller
from flask_login import login_required

home_router = Blueprint('home_router', __name__)

@home_router.route('/',methods=['GET'])
@login_required
def home():
    return homecontroller.index()
