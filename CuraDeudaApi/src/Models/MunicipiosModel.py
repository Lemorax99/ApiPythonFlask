from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()

db = SQLAlchemy()

class Municipios(db.Model):
    id_municipio = db.Column(db.Integer,primary_key=True)
    d_mnpio = db.Column(db.String(50),unique=True)

    def __init__(self,d_mnpio):
        self.d_mnpio = d_mnpio

class MunicipioSchema(ma.Schema):
    class Meta:
        fields = ('id_municipio','d_mnpio')

municipio_schema = MunicipioSchema()

municipios_schema = MunicipioSchema(many=True)