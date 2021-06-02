from flask import Blueprint
from app.controllers.AuthController import authcontroller

auth_router = Blueprint('auth_router', __name__)

@auth_router.route('/login',methods=['GET'])
def login():
    return authcontroller.loginGet()
@auth_router.route('/signup',methods=['GET'])
def signup():
    return authcontroller.signupGet()

@auth_router.route('/login',methods=['POST'])
def loginp():
    return authcontroller.login()

@auth_router.route('/register',methods=['POST'])
def register():
    return authcontroller.register()