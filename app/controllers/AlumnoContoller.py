from flask import render_template

class AlumnoController():
    def __init__(self):
        pass

    def index(self):
        from app.models.Alumno import Alumno
        alumnos = Alumno.query.all()
        return render_template('alumnos.html', alumnos=alumnos)
    
    def insert(self):
        return render_template('alumnos.html', alumnos=alumnos)


alumnocontroller = AlumnoController()