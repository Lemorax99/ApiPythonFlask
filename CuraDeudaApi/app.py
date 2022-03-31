from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})

@app.route('/products',methods=['GET'])
def products():
    return "hola"

@app.route('/products/<string:product_name>')
def getproduct(product_name):
    print (product_name)
    return "product"

if __name__ == "__main__":
    app.run (debug=True, port=4000)