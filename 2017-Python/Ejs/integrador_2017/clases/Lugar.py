import pymysql
from .Coordenada import coordenada

class lugar (object):
    codigo = None
    nombre = None
    coordenadas = []

    def crear_coordenada(self , latitud , longitud , lugar):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        mi_coordenada = coordenada()

        cursor.execute("insert into coordenada values (NULL , '" + str(latitud) + "' , '" + str(longitud) + "')")
        codigo_coordenada = cursor.lastrowid

        if lugar.soy() == "continente":
            print("asdasdasd")
            cursor.execute("insert into continente_has_coordenada values ('" + str(lugar.codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")

        elif lugar.soy() == "pais":
            cursor.execute("insert into pais_has_coordenada values ('" + str(lugar.codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")

        elif lugar.soy() == "provincia":
            cursor.execute("insert into provincia_has_coordenada values ('" + str(lugar.codigo) + "' ,"
                           " '" + str( codigo_coordenada) + "')")


        elif lugar.soy() == "ciudad":
            cursor.execute("insert into ciudad_has_coordenada values ('" + str(lugar.codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")

        elif lugar.soy() == "barrio":
            cursor.execute("insert into barrio_has_coordenada values ('" + str(lugar.codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")

        mi_coordenada.codigo = codigo_coordenada
        mi_coordenada.latitud = latitud
        mi_coordenada.longitud = longitud

        return mi_coordenada
