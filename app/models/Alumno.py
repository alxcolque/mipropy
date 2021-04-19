from flask_sqlalchemy import SQLAlchemy
from app import db

#La clase Registromaterias es el modelo de asociacion 
# #entre dos modelos que lleva atributos
class Registromaterias(db.Model):
    __tablename__ = 'registromaterias'
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), primary_key=True)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), primary_key=True)
    paralelo = db.Column(db.String(1))

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    celular = db.Column(db.String(20))
