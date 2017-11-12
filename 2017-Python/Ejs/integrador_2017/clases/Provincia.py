import pymysql
from .Lugar import lugar
from .Ciudad import ciudad

class provincia (lugar):

    pais_perteneciente = []


    def soy(cls):
        return "provincia"

    def crear_ciudad(self, nombre , lista_coordenadas):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        mi_ciudad = ciudad()

        cursor.execute("insert into ciudad values (NULL , '" + str(nombre) + "' , '" + str(self.codigo) + "')")
        codigo = cursor.lastrowid

        mi_ciudad.codigo = codigo
        mi_ciudad.nombre = nombre
        mi_ciudad.provincia_perteneciente = self.codigo
        mi_ciudad.coordenadas = lista_coordenadas

        for item in lista_coordenadas:
            print(item)
            print(item[0])
            self.crear_coordenada(item[0][0] , item[0][1] , mi_ciudad)

        return mi_ciudad