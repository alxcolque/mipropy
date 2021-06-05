from flask import Blueprint
from app.controllers.CarruselController import carruselcontroller
from flask_login import login_required

carrusel_router = Blueprint('carrusel_router', __name__)

@carrusel_router.route('/carruseles',methods=['GET'])
@login_required
def main():
    return carruselcontroller.index()
@carrusel_router.route('/carruseles/crear',methods=['GET'])
@login_required
def crear():
    return carruselcontroller.crearCarrusel()
@carrusel_router.route('/guardar_carrusel',methods=['POST'])
@login_required
def create():
    return carruselcontroller.guardarCarrusel()

@carrusel_router.route('/eliminar/<string:id>')
@login_required
def eliminar(id):
    return carruselcontroller.eliminarCarrusel(id)

@carrusel_router.route('/editar/<string:id>')
@login_required
def editar(id):
    return carruselcontroller.editarCarrusel(id)

@carrusel_router.route('/actualizar/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return carruselcontroller.actualizarCarrusel(id)
