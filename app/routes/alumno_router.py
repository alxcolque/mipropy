from flask import Blueprint
from app.controllers.AlumnoContoller import alumnocontroller

alumno_router = Blueprint('alumno_router', __name__)

@alumno_router.route('/alumnos',methods=['GET'])
def alumno():
    return alumnocontroller.index()