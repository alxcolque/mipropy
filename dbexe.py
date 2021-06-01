from app.models.User import User
from app.models.Alumno import Alumno
from app.models.Materia import Materia
from app.models.Clase import Clase
from app.models.Practica import Practica
from app.models.Carrusel import Carrusel

from app import db

db.drop_all()
db.create_all()

""" alumno = Alumno(nombres='Pedro',apellidos = 'Smith', email = 'pedro@mail.com', celular='7634566')
db.session.add(alumno)
db.session.commit()  """
