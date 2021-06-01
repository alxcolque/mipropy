from flask import Blueprint
from app.controllers.CarruselController import carruselcontroller

carrusel_router = Blueprint('carrusel_router', __name__)

@carrusel_router.route('/carruseles',methods=['GET'])
def main():
    return carruselcontroller.index()
@carrusel_router.route('/carruseles/crear',methods=['GET'])
def crear():
    return carruselcontroller.crearCarrusel()
@carrusel_router.route('/guardar_carrusel',methods=['POST'])
def create():
    return carruselcontroller.guardarCarrusel()

@carrusel_router.route('/eliminar/<string:id>')
def eliminar(id):
    return carruselcontroller.eliminarCarrusel(id)

@carrusel_router.route('/editar/<string:id>')
def editar(id):
    return carruselcontroller.editarCarrusel(id)

@carrusel_router.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    return carruselcontroller.actualizarCarrusel(id)
