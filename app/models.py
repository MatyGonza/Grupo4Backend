from app.database import get_db

class Productos:

    #constuctor
    def __init__(self,id_producto=None,nombre=None,tipo=None,imagen=None):
        self.id_producto=id_producto
        self.nombre=nombre
        self.tipo=tipo
        self.imagen=imagen

    def serialize(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'imagen': self.imagen
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM productos"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        movies = [Productos(id_producto=row[0], nombre=row[1], tipo=row[2], release_date=row[3], imagen=row[4]) for row in rows]

        # movies = []
        # for row in rows:
        #     new_movie = Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4])
        #     movies.append(new_movie)

        cursor.close()
        return movies
        

    def get_by_id(id_movie):
        pass

    def save():
        pass

    def delete():
        pass
