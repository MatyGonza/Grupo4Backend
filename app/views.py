from flask import jsonify, request
from app.models import Producto

def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

def get_all_productos():
    productos = Producto.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)


def get_producto(id):
    producto = Producto.get_by_id(id)
    if not producto:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(producto.serialize())


def create_producto():
    #recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_producto = Producto(
        nombre=data['nombre'],
        tipo=data['tipo'],
        precio=data['precio'],
        imagen=data['imagen']
    )
    new_producto.save()
    return jsonify({'message':'Producto creado con exito'}), 201
    

def update_producto():
    pass

def delete_producto():
    pass