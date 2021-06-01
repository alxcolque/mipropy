from flask import Blueprint
from app.controllers.PracticaController import practicacontroller

practica_router = Blueprint('practica_router', __name__)

@practica_router.route('/practicas',methods=['GET'])
def principal():
    return practicacontroller.index()
@practica_router.route('/practicas/crear',methods=['GET'])
def crear():
    return practicacontroller.crearPractica()
@practica_router.route('/practicas/guardarp',methods=['POST'])
def guardar():
    return practicacontroller.guardarPractica()

@practica_router.route('/practicas/eliminarpractica/<string:id>')
def eliminar(id):
    return practicacontroller.eliminarPractica(id)

@practica_router.route('/practicas/editar/<string:id>')
def editar(id):
    return practicacontroller.editarPractica(id)

@practica_router.route('/practicas/actualizarpractica/<id>',methods=['POST'])
def actualizar(id):
    return practicacontroller.actualizarPractica(id)
