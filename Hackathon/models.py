from flask import Flask
from peewee import *
import os


app = Flask(__name__)
app.config ["SECRET_KEY"] = "KALIF44528SSJ"


arq = 'tracksoft.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nome = CharField()
    cpf = CharField()
    senha = CharField()
    foto = TextField()
    telefone = CharField()

class Camera(BaseModel):
    identificador = IntegerField()
    rua = CharField()
    numero = IntegerField()
    bairro = CharField()
    cidade = CharField()
    UF = CharField()

class Veiculo(BaseModel):
    marca = CharField()
    modelo = CharField()
    cor = CharField()
    placa = CharField()
    ano = IntegerField()
    foto = CharField()
    descricao = TextField()

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Usuario, Camera, Veiculo])
