from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json

#Importación de los modelos y esquemas de datos
from Models.EstadosModel import Estados,estado_schema,estados_schema
from Models.MunicipiosModel import Municipios,municipio_schema,municipios_schema
from Models.Colonias import Colonias,colonia_schema,colonias_schema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/sepomex'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
#==============================================================================================
# ===========  CRUD PARA OPERACIONES BASICAS DE LOS ESTADOS  ==================================
#==============================================================================================
#Adicionar estados
@app.route('/Estados',methods=['POST'])
def crear_Estado():

    c_estado = request.json['c_estado']
    d_estado = request.json['d_estado']

    new_estado = Estados(c_estado,d_estado)
    db.session.add(new_estado)
    db.session.commit()

    return estado_schema.jsonify(new_estado)
#Ver todos los estados
@app.route('/Estados',methods=['GET'])
def get_Estados():

    all_estados = Estados.query.all()
    result = estados_schema.dump(all_estados)

    return jsonify(result),200
#Buscar Id estado
@app.route('/Estados/<id>',methods=['GET'])
def get_Estado(id):
    estado = Estados.query.get(id)

    return estado_schema.jsonify(estado)
#Actualiar estado
@app.route('/Estados/<id>',methods=['PUT'])
def put_Estado(id):
    estado = Estados.query.get(id)

    c_estado = request.json['c_estado']
    d_estado = request.json['d_estado']

    estado.c_estado = c_estado
    estado.d_estado = d_estado

    db.session.commit()

    return estado_schema.jsonify(estado)
#Eliminar estado
@app.route('/Estados/<id>',methods=['DELETE'])
def del_Estado(id):
    estado = Estados.query.get(id)
    db.session.delete(estado)
    db.session.commit()

    return estado_schema.jsonify(estado)


#==============================================================================================
# ===========  CRUD PARA OPERACIONES BASICAS DE LOS MUNICIPIOS  ===============================
#==============================================================================================

#Adicionar municipio
@app.route('/Municipios',methods=['POST'])
def crear_Municipio():

    d_mnpio = request.json['d_mnpio']

    new_municipio = Municipios(d_mnpio)
    db.session.add(new_municipio)
    db.session.commit()

    return municipio_schema.jsonify(new_municipio)

#Ver todos los municipios
@app.route('/Municipios',methods=['GET'])
def get_Municipios():

    all_municipios = Municipios.query.all()
    result = municipios_schema.dump(all_municipios)

    return jsonify(result),200

#Buscar Id municipio
@app.route('/Municipios/<id>',methods=['GET'])
def get_Municipio(id):
    municipio = Municipios.query.get(id)

    return municipio_schema.jsonify(municipio)

#Actualiar estado
@app.route('/Municipios/<id>',methods=['PUT'])
def put_Municipio(id):
    municipio = Municipios.query.get(id)

    d_mnpio = request.json['d_mnpio']

    municipio.d_mnpio = d_mnpio

    db.session.commit()

    return estado_schema.jsonify(municipio)

#Eliminar estado
@app.route('/Municipios/<id>',methods=['DELETE'])
def del_Municipio(id):
    municipio = Municipios.query.get(id)
    db.session.delete(municipio)
    db.session.commit()

    return estado_schema.jsonify(municipio)

#==============================================================================================
# ===========  CRUD PARA OPERACIONES BASICAS DE LAS COLONIAS  =================================
#==============================================================================================

@app.route('/Colonias',methods=['POST'])
def crear_Colonia():

    id_estado = request.json['id_estado']
    id_municipio = request.json['id_municipio']
    d_asenta = request.json['d_asenta']
    d_codigo = request.json['d_codigo']

    new_colonia = Colonias(id_estado,id_municipio,d_asenta,d_codigo)
    db.session.add(new_colonia)
    db.session.commit()

    return colonia_schema.jsonify(new_colonia)



#==============================================================================================
# ===========  TODOS LOS DATOS MEDIANTE QUERYS  ===============================================
#==============================================================================================


#llamadas para obtener todos los datos btencion de recursos

@app.route('/',methods=['GET'])
def ver_Todo():
    response=[]
    query = db.session.query(Colonias,Municipios,Estados).filter( Estados.id_estado == Colonias.id_estado).filter(Municipios.id_municipio == Colonias.id_municipio).all()
    for c,m,e in query:
        response.append({"id_colonia":c.id_colonia,"id_estado":c.id_estado,"id_municipio":c.id_municipio,"d_asenta":c.d_asenta,
                            "d_codigo":c.d_codigo,"c_estado":e.c_estado,"d_estado":e.d_estado,"d_mnpio":m.d_mnpio})

    return jsonify(response)

#Obtener colonia por codigo postal
@app.route('/Colonia/<CP>',methods=['GET'])
def ver_ColoniasxCP(CP):
    response=[]
    query = db.session.query(Colonias,Municipios,Estados).filter(Colonias.d_codigo == CP).filter( Estados.id_estado == Colonias.id_estado).filter(Municipios.id_municipio == Colonias.id_municipio).all()
    for c,m,e in query:
        response.append({"id_colonia":c.id_colonia,"id_estado":c.id_estado,"id_municipio":c.id_municipio,"d_asenta":c.d_asenta,
                            "d_codigo":c.d_codigo,"c_estado":e.c_estado,"d_estado":e.d_estado,"d_mnpio":m.d_mnpio})

    return jsonify(response)

#Obtener colonia por nombre
@app.route('/NombreColonia/<Nombre>',methods=['GET'])
def ver_ColoniaxNombre(Nombre):
    response=[]
    query = db.session.query(Colonias,Municipios,Estados).filter(Colonias.d_asenta == Nombre).filter( Estados.id_estado == Colonias.id_estado).filter(Municipios.id_municipio == Colonias.id_municipio).all()
    for c,m,e in query:
        response.append({"id_colonia":c.id_colonia,"id_estado":c.id_estado,"id_municipio":c.id_municipio,"d_asenta":c.d_asenta,
                            "d_codigo":c.d_codigo,"c_estado":e.c_estado,"d_estado":e.d_estado,"d_mnpio":m.d_mnpio})

    return jsonify(response)

#Obtener estado por nombre
@app.route('/NombreEstado/<Nombre>',methods=['GET'])
def ver_EstadoxNombre(Nombre):
    response=[]
    query = db.session.query(Colonias,Municipios,Estados).filter(Estados.d_estado == Nombre).filter( Estados.id_estado == Colonias.id_estado).filter(Municipios.id_municipio == Colonias.id_municipio).all()
    for c,m,e in query:
        response.append({"id_colonia":c.id_colonia,"id_estado":c.id_estado,"id_municipio":c.id_municipio,"d_asenta":c.d_asenta,
                            "d_codigo":c.d_codigo,"c_estado":e.c_estado,"d_estado":e.d_estado,"d_mnpio":m.d_mnpio})

    return jsonify(response)

#Obtener municipio por nombre
@app.route('/NombreMunicipio/<Nombre>',methods=['GET'])
def ver_MunicipioxNombre(Nombre):
    response=[]
    query = db.session.query(Colonias,Municipios,Estados).filter(Municipios.d_mnpio == Nombre).filter( Estados.id_estado == Colonias.id_estado).filter(Municipios.id_municipio == Colonias.id_municipio).all()
    for c,m,e in query:
        response.append({"id_colonia":c.id_colonia,"id_estado":c.id_estado,"id_municipio":c.id_municipio,"d_asenta":c.d_asenta,
                            "d_codigo":c.d_codigo,"c_estado":e.c_estado,"d_estado":e.d_estado,"d_mnpio":m.d_mnpio})

    return jsonify(response)


if __name__ == "__main__":
    app.run (debug=True, port=4000)