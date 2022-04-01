from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()

db = SQLAlchemy()

class Estados(db.Model):
    id_estado = db.Column(db.Integer,primary_key=True)
    c_estado = db.Column(db.String(5),unique=True)
    d_estado = db.Column(db.String(50),unique=False)

    def __init__(self,c_estado,d_estado):
        self.c_estado = c_estado
        self.d_estado = d_estado

class EstadoSchema(ma.Schema):
    class Meta:
        fields = ('id_estado','c_estado','d_estado')

estado_schema = EstadoSchema()

estados_schema = EstadoSchema(many=True)