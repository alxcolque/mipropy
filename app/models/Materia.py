from flask_sqlalchemy import SQLAlchemy
from app import db

class Materia(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    sigla = db.Column(db.String(50))
    # Referencia de relacion con modelos externos
    practicas = db.relationship(
        'Practica', backref='materia', lazy='dynamic')
    clases = db.relationship(
        'Clase', backref='materia', lazy='dynamic')

