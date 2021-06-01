from flask import Blueprint
from app.controllers.MateriaController import materiacontroller

materia_router = Blueprint('materia_router', __name__)

@materia_router.route('/materias',methods=['GET'])
def principal():
    return materiacontroller.index()
@materia_router.route('/materias/crear',methods=['GET'])
def crear():
    return materiacontroller.crearMateria()
@materia_router.route('/materias/guardar',methods=['POST'])
def guardar():
    return materiacontroller.guardarMateria()

@materia_router.route('/materias/eliminarmateria/<string:id>')
def eliminar(id):
    return materiacontroller.eliminarMateria(id)

@materia_router.route('/materias/editar/<string:id>')
def editar(id):
    return materiacontroller.editarMateria(id)

@materia_router.route('/materias/actualizarmateria/<id>',methods=['POST'])
def actualizar(id):
    return materiacontroller.actualizarMateria(id)
