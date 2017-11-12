import pymysql
from .Lugar import lugar
from .Pais import pais

class continente (lugar):
    pass

    def soy(cls):
        return "continente"

    def crear_pais(self, nombre , lista_coordenadas):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        mi_pais = pais()

        cursor.execute("insert into pais values (NULL , '" + str(nombre) + "' , '" + str(self.codigo) + "')")
        codigo = cursor.lastrowid

        mi_pais.codigo = codigo
        mi_pais.nombre = nombre
        mi_pais.pais_perteneciente = self.codigo
        mi_pais.coordenadas = lista_coordenadas

        for item in lista_coordenadas:
            print(item)
            print(item[0])
            self.crear_coordenada(item[0][0] , item[0][1] , mi_pais)

        return mi_pais