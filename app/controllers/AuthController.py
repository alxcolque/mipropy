from app import db, bcrypt
from flask import render_template, request, redirect, url_for, flash, session
from app.models.User import User

class AuthController():
    def __init__(self):
        pass

    def loginGet(self):
        return render_template('auth/login.html')
    def signupGet(self):
        return render_template('auth/signup.html')
    def login(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            fecha = request.form['fecha']
            materia_id = request.values['materia_id']
            
            user = User(nombre=nombre, descripcion=descripcion, fecha=fecha, materia_id=materia_id)
            db.session.add(user)
            db.session.commit()
            flash('Materia creado exitosamente')
            return redirect(url_for('user_router.principal'))
    def register(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']
            password = bcrypt.generate_password_hash(request.form['password'])
            
            user = User(nombre=nombre, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return redirect(url_for('alumno_router.alumnos'))
    

authcontroller = AuthController()
