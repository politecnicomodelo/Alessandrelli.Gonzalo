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

        for item in lista_coordenadas:
            cursor.execute("insert into coordenada values (NULL , '" + str(item[0]) + "') , '" + str(item[1]) + "')")
            codigo_coordenada = cursor.lastrowid
            cursor.execute("insert into pais_has_coordenada values ('" + str(codigo) + "' ,"
                           " '" + str(codigo_coordenada) + "')")
            item.codigo = codigo_coordenada

        mi_pais.codigo = codigo
        mi_pais.nombre = nombre
        mi_pais.pais_perteneciente = self.codigo
        mi_pais.coordenadas = lista_coordenadas

        return mi_pais