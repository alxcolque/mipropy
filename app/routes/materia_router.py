from flask import Blueprint
from app.controllers.MateriaController import materiacontroller
from flask_login import login_required

materia_router = Blueprint('materia_router', __name__)

@materia_router.route('/materias',methods=['GET'])
@login_required
def principal():
    return materiacontroller.index()
@materia_router.route('/materias/crear',methods=['GET'])
@login_required
def crear():
    return materiacontroller.crearMateria()
@materia_router.route('/materias/guardar',methods=['POST'])
@login_required
def guardar():
    return materiacontroller.guardarMateria()

@materia_router.route('/materias/eliminarmateria/<string:id>')
@login_required
def eliminar(id):
    return materiacontroller.eliminarMateria(id)

@materia_router.route('/materias/editar/<string:id>')
@login_required
def editar(id):
    return materiacontroller.editarMateria(id)

@materia_router.route('/materias/actualizarmateria/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return materiacontroller.actualizarMateria(id)
