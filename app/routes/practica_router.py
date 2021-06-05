from flask import Blueprint
from app.controllers.PracticaController import practicacontroller
from flask_login import login_required

practica_router = Blueprint('practica_router', __name__)

@practica_router.route('/practicas',methods=['GET'])
@login_required
def principal():
    return practicacontroller.index()
@practica_router.route('/practicas/crear',methods=['GET'])
@login_required
def crear():
    return practicacontroller.crearPractica()
@practica_router.route('/practicas/guardarp',methods=['POST'])
@login_required
def guardar():
    return practicacontroller.guardarPractica()

@practica_router.route('/practicas/eliminarpractica/<string:id>')
@login_required
def eliminar(id):
    return practicacontroller.eliminarPractica(id)

@practica_router.route('/practicas/editar/<string:id>')
@login_required
def editar(id):
    return practicacontroller.editarPractica(id)

@practica_router.route('/practicas/actualizarpractica/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return practicacontroller.actualizarPractica(id)
