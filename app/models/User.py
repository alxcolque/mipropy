from flask_sqlalchemy import SQLAlchemy
from app import app
from app import db

class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key = True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    celular = db.Column(db.String(50))

    def __init__(self, nombre, email, celular):
        self.nombre = nombre
        self.email = email
        self.celular = celular

    