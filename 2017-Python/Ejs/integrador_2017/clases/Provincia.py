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

        for item in lista_coordenadas:
            cursor.execute("insert into coordenada values (NULL , '" + str(item[0]) + "') , '" + str(item[1]) + "')")
            codigo_coordenada = cursor.lastrowid
            cursor.execute("insert into ciudad_has_coordenada values ('" + str(codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")
            item.codigo = codigo_coordenada

        mi_ciudad.codigo = codigo
        mi_ciudad.nombre = nombre
        mi_ciudad.provincia_perteneciente = self.codigo
        mi_ciudad.coordenadas = lista_coordenadas

        return mi_ciudad