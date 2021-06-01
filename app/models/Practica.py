from flask_sqlalchemy import SQLAlchemy
from app import db

class Entregapracticas(db.Model):
    __tablename__ = 'entregapracticas'
    alumno_id = db.Column(db.Integer, db.ForeignKey(
        'alumnos.id'), primary_key=True)
    practica_id = db.Column(db.Integer, db.ForeignKey(
        'practicas.id'), primary_key=True)
    fechaentrega = db.Column(db.DateTime)
    calificacion = db.Column(db.Float())


class Practica(db.Model):
    __tablename__ = 'practicas'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    # Atributo o la clave foranea
    materia_id = db.Column(db.Integer, db.ForeignKey(
        'materias.id'), nullable=False)
    alumno = db.relationship("Entregapracticas")
