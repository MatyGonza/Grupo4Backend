from flask import jsonify
from app.models import Productos

def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

def get_all_productos():
    productos = Productos.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)


def get_producto(id_producto):
    producto = Productos.get_by_id(id_producto)
    if not producto:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(producto.serialize())


def create_producto():
    pass

def update_producto():
    pass

def delete_producto():
    pass