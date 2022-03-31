from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()

db = SQLAlchemy()

class Colonias(db.Model):
    id_colonia = db.Column(db.Integer,primary_key=True) 
    id_estado = db.Column(db.Integer)
    id_municipio = db.Column(db.Integer)
    d_asenta = db.Column(db.String(50),unique=True)
    d_codigo = db.Column(db.String(5),unique=False)

    def __init__(self, id_estado, id_municipio, d_asenta, d_codigo):
        self.id_estado = id_estado
        self.id_municipio = id_municipio
        self.d_asenta = d_asenta
        self.d_codigo = d_codigo

class ColoniaSchema(ma.Schema):
    class Meta:
        fields = ('id_colonia','id_estado','id_municipio','d_asenta','d_codigo')

colonia_schema = ColoniaSchema()

colonias_schema = ColoniaSchema(many=True)