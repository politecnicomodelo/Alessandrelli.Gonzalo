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
        codigos = cursor.fetchall()
        print("asdasdasd")

        for codigo in codigos:
            cursor.execute("delete from barrio_has_coordenada where barrio_codigo = '" + str(self.codigo) + "'")
            cursor.execute("delete from coordenada where codigo = '" + str(codigo[0]) + "'")

        cursor.execute("delete from barrio where codigo = '" + str(self.codigo) + "'")

    def eliminar_coordenada (self , codigo_coordenada):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        cursor.execute("delete from barrio_has_coordenada where coordenada_codigo = '" +
                       str(codigo_coordenada) + "'")
        cursor.execute("delete from coordenada where codigo = '" +
                       str(codigo_coordenada) + "'")

    def actualizar_nombre (self , nombre):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        cursor.execute("update barrio set nombre = '" +str(nombre) + "' where codigo = '" + str(self.codigo) + "'")

    def actualizar_poblacion (self , poblacion):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        cursor.execute("update barrio set poblacion = '" +str(poblacion) + "' where codigo = '" + str(self.codigo) + "'")