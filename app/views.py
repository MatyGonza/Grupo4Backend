from flask import jsonify
from app.models import Productos

def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

def get_all_productos():
    productos = Productos.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)

def get_producto():
    pass

def create_producto():
    pass

def update_producto():
    pass

def delete_producto():
    pass