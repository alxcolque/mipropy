from flask import Blueprint
from app.controllers.AlumnoContoller import alumnocontroller
from flask_login import login_required

alumno_router = Blueprint('alumno_router', __name__)

@alumno_router.route('/alumnos',methods=['GET'])
@login_required
def alumnos():
    return alumnocontroller.index()


@alumno_router.route('/crear_alumno',methods=['POST'])
@login_required
def crear():
    return alumnocontroller.crearAlumno()

@alumno_router.route('/eliminar/<string:id>')
@login_required
def eliminar(id):
    return alumnocontroller.eliminarAlumno(id)

@alumno_router.route('/editar/<string:id>')
@login_required
def editar(id):
    return alumnocontroller.editarAlumno(id)
#Modificar registro
@alumno_router.route('/actualizar/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return alumnocontroller.actualizarAlumno(id)