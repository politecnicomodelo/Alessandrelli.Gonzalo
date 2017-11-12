import pymysql
from .Lugar import lugar
from .Provincia import provincia

class pais (lugar):
    continente_perteneciente = []


    def soy(cls):
        return "pais"

    def crear_provincia(self, nombre , lista_coordenadas):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        mi_provincia = provincia()

        cursor.execute("insert into provincia values (NULL , '" + str(nombre) + "' , '" + str(self.codigo) + "')")
        codigo = cursor.lastrowid

        mi_provincia.codigo = codigo
        mi_provincia.nombre = nombre
        mi_provincia.pais_perteneciente = self.codigo
        mi_provincia.coordenadas = lista_coordenadas

        for item in lista_coordenadas:
            print(item)
            print(item[0])
            self.crear_coordenada(item[0][0] , item[0][1] , mi_provincia)

        return mi_provincia