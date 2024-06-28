from app.database import get_db

class Producto:

    #constuctor
    def __init__(self,id=None,nombre=None,tipo=None,precio=None,imagen=None):
        self.id=id
        self.nombre=nombre
        self.tipo=tipo
        self.precio=precio
        self.imagen=imagen

    def serialize(self):
        return {
            'id': self.id,
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
        print(rows)

        productos = [Producto(id=row[0], nombre=row[1], tipo=row[2], precio=row[3], imagen=row[4]) for row in rows]

        cursor.close()
        return productos
        
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id=row[0], nombre=row[1], tipo=row[2],precio=row[3], imagen=row[4])
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                UPDATE productos SET nombre = %s, tipo = %s, precio = %s, imagen = %s
                WHERE id = %s
            """, (self.nombre, self.tipo, self.precio, self.imagen, self.id))
        else:
            cursor.execute("""
                INSERT INTO productos (nombre, tipo, precio, imagen) VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.tipo, self.precio, self.imagen))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete():
        pass
