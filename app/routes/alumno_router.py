from flask import Blueprint
from app.controllers.AlumnoContoller import alumnocontroller

alumno_router = Blueprint('alumno_router', __name__)

@alumno_router.route('/alumnos',methods=['GET'])
def alumnos():
    return alumnocontroller.index()


@alumno_router.route('/crear_alumno',methods=['POST'])
def crear():
    return alumnocontroller.crearAlumno()

@alumno_router.route('/eliminar/<string:id>')
def eliminar(id):
    return alumnocontroller.eliminarAlumno(id)

@alumno_router.route('/editar/<string:id>')
def editar(id):
    return alumnocontroller.editarAlumno(id)
#Modificar registro
@alumno_router.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    return alumnocontroller.actualizarAlumno(id)