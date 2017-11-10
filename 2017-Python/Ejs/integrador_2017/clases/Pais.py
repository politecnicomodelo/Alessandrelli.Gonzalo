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

        for item in lista_coordenadas:
            cursor.execute("insert into coordenada values (NULL , '" + str(item[0]) + "') , '" + str(item[1]) + "')")
            codigo_coordenada = cursor.lastrowid
            cursor.execute("insert into provincia_has_coordenada values ('" + str(codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")
            item.codigo = codigo_coordenada

        mi_provincia.codigo = codigo
        mi_provincia.nombre = nombre
        mi_provincia.pais_perteneciente = self.codigo
        mi_provincia.coordenadas = lista_coordenadas

        return mi_provincia