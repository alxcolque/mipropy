from app import db
from flask import render_template, request, redirect, url_for, flash
from app.models.Materia import Materia
from app.models.Practica import Practica
from app.models.Alumno import Alumno

class PracticaController():
    def __init__(self):
        pass

    def index(self):
        practicas = Practica.query.join(Materia).filter().all()
        return render_template('practicas/index.html', title='Practicas', practicas=practicas)
    def crearPractica(self):
        materias = Materia.query.all()
        return render_template('/practicas/create.html', title='Nuevo practica', materias=materias)
    def guardarPractica(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            fecha = request.form['fecha']
            materia_id = request.values['materia_id']
            
            practica = Practica(nombre=nombre, descripcion=descripcion, fecha=fecha, materia_id=materia_id)
            db.session.add(practica)
            db.session.commit()
            flash('Materia creado exitosamente')
            return redirect(url_for('practica_router.principal'))

    def eliminarPractica(self, _id):
        practica = Practica.query.get(_id)
        db.session.delete(practica)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('practica_router.principal'))

    def editarPractica(self, _id):
        practica = Practica.query.get(_id)
        materias = Materia.query.all()
        return render_template('practicas/edit.html', title='Editar', practica=practica, materias=materias)

    def actualizarPractica(self, _id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            fecha = request.form['fecha']
            materia_id = request.form['materia_id']

            practica = Practica.query.get(_id)
            practica.nombre=nombre 
            practica.descripcion=descripcion
            practica.fecha=fecha
            practica.materia_id=materia_id

            db.session.commit()
            flash('Actualizado con exito')
            return redirect(url_for('practica_router.principal'))

practicacontroller = PracticaController()
