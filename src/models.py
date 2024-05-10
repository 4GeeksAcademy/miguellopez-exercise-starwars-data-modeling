import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    fecha_de_subscripcion = Column(DateTime, nullable=False)
    email = Column(String(100), nullable=False)
    favoritos = Column(Integer)

class Planetas(Base):
    __tablename__ = 'planetas'
    id_planeta = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(100), nullable=False)
    periodo_rotacion = Column(Integer, nullable=False)
    diametro = Column(Float, nullable=False)
    clima = Column(String(50), nullable=False)
    terreno = Column(String(50), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship(Usuario)

class Nombres(Base):
    __tablename__ = 'personas'
    id_persona = Column(Integer, primary_key=True)
    nombre_persona = Column(String(100), nullable=False)
    peso = Column(Integer, nullable=False)
    color_de_piel = Column(String(20), nullable=False)
    color_de_pelo = Column(String(20))
    genero = Column(String(20))
    birth_year = Column(Integer, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship(Usuario)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id_vehiculos = Column(Integer, primary_key=True)
    nombre_vehiculos = Column(String(100), nullable=False)
    modelo = Column(String(50), nullable=False)
    longitud = Column(Float, nullable=False)
    tripulacion = Column(Integer, nullable=False)
    clase_de_vehiculo = Column(String, nullable=False)
    capacidad_de_carga = Column(Integer, nullable=False)
    velocidad_maxima = Column(Integer, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship(Usuario)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
