from flask import Blueprint
from app.controllers.PrincipalController import principalcontroller

principal_router = Blueprint('principal_router', __name__)

@principal_router.route('/',methods=['GET'])
def principal():
    return principalcontroller.index()