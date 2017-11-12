import pymysql
from .Lugar import lugar

class barrio (lugar):
    poblacion = None
    ciudad_perteneciente = None

    def soy(cls):
        return "barrio"

    def eliminar_objetos_relacionados(self):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        cursor.execute("select coordenada_codigo from barrio_has_coordenada where barrio_codigo = '" + str(
            self.codigo) + "'")
        codigo = cursor.fetchall()
        codigo = codigo[0]

        cursor.execute("delete from barrio_has_coordenada where barrio_codigo = '" + str(self.codigo) + "'")
        cursor.execute("delete from coordenada where codigo = '" + str(codigo) + "'")
        cursor.execute("delete from barrio where codigo = '" + str(self.codigo) + "'")