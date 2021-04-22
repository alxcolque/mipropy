from flask import render_template, request, flash, redirect, url_for
from app import db

class AlumnoController():
    def __init__(self):
        pass

    def index(self):
        from app.models.Alumno import Alumno
        alumnos = Alumno.query.all()
        return render_template('alumnos.html', alumnos=alumnos)
    
    def crearAlumno(self):
        if request.method == 'POST':
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            email = request.form['email']
            celular = request.form['celular']

            from app.models.Alumno import Alumno
            alumno = Alumno(nombres = nombres, apellidos = apellidos, email = email, celular = celular)
            db.session.add(alumno)
            db.session.commit()

            flash('Registro exitoso')
            return redirect(url_for('alumno_router.alumnos'))

    def eliminarAlumno(self, _id):
        from app.models.Alumno import Alumno
        alumno = Alumno.query.get(_id)
        db.session.delete(alumno)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('alumno_router.alumnos'))


alumnocontroller = AlumnoController()