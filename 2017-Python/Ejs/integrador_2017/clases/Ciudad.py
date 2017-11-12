import pymysql
from .Lugar import lugar
from .Barrio import barrio

class ciudad (lugar):
    provincia_perteneciente = []


    def soy(cls):
        return "ciudad"

    def crear_barrio(self , nombre , poblacion , lista_coordenadas):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        mi_barrio = barrio()

        cursor.execute ("insert into barrio values (NULL , '" + str(nombre) + "' , '" + str(poblacion) + "' "
                        ", '" + str(self.codigo) + "')")
        codigo = cursor.lastrowid


        mi_barrio.codigo = codigo
        mi_barrio.nombre = nombre
        mi_barrio.poblacion = poblacion
        mi_barrio.ciudad_perteneciente = self.codigo
        mi_barrio.coordenadas = lista_coordenadas

        for item in lista_coordenadas:
            print(item)
            print(item[0])
            self.crear_coordenada(item[0][0] , item[0][1] , mi_barrio)

        return mi_barrio

