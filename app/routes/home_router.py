from flask import Blueprint
from app.controllers.HomeController import homecontroller

home_router = Blueprint('home_router', __name__)

@home_router.route('/',methods=['GET'])
def home():
    return homecontroller.index()
