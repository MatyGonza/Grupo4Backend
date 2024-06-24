from app.database import get_db

class Productos:

    #constuctor
    def __init__(self,id_producto=None,nombre=None,tipo=None,precio=None,imagen=None):
        self.id_producto=id_producto
        self.nombre=nombre
        self.tipo=tipo
        self.precio=precio
        self.imagen=imagen

    def serialize(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio':self.precio,
            'imagen': self.imagen
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM productos"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        productos = [Productos(id_producto=row[0], nombre=row[1], tipo=row[2], precio=row[3], imagen=row[4]) for row in rows]

        cursor.close()
        return productos
        
    @staticmethod
    def get_by_id(id_producto):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id_producto))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Productos(id_producto=row[0], nombre=row[1], tipo=row[2],precio=row[3], imagen=row[4])
        return None

    def save():
        pass

    def delete():
        pass
