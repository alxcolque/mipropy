from app import db
from flask import render_template, request, redirect, url_for, flash
from app.models.Materia import Materia
from app.models.Practica import Practica
from app.models.Clase import Clase
from app.models.Alumno import Alumno

class MateriaController():
    def __init__(self):
        pass

    def index(self):
        
        materias = Materia.query.all()
        return render_template('materias/index.html', title='Materias', materias=materias)
    def crearMateria(self):
        return render_template('materias/create.html', title='Nuevo materia')
    def guardarMateria(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            sigla = request.form['sigla']
            
            materia = Materia(nombre=nombre, sigla=sigla)
            db.session.add(materia)
            db.session.commit()

            flash('Materia creado exitosamente')
            return redirect(url_for('materia_router.principal'))

    def eliminarMateria(self, _id):
        materia = Materia.query.get(_id)
        db.session.delete(materia)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('materia_router.principal'))

    def editarMateria(self, _id):
        materia = Materia.query.get(_id)
        return render_template('materias/edit.html', title='Editar', materia=materia)

    def actualizarMateria(self, _id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            sigla = request.form['sigla']

            materia = Materia.query.get(_id)
            materia.nombre=nombre 
            materia.sigla=sigla

            db.session.commit()
            flash('Actualizado con exito')
            return redirect(url_for('materia_router.principal'))

materiacontroller = MateriaController()
