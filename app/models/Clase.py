from flask_sqlalchemy import SQLAlchemy
from app import db

# Relacion de Muchos a Muchos
detalleclases = db.Table('detalleclases',
    db.Column('alumno_id', db.Integer, db.ForeignKey(
        'alumnos.id'), primary_key=True),
    db.Column('clase_id', db.Integer, db.ForeignKey(
        'clases.id'), primary_key=True)
)

class Clase(db.Model):
    __tablename__ = 'clases'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    # Atributo o la clave foranea
    materia_id = db.Column(db.Integer, db.ForeignKey(
        'materias.id'), nullable=False)

        


