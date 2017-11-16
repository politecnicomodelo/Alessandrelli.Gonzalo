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


    def objetos_a_eliminar (self , lista_provincias , lista_ciudades , lista_barrios):

        mi_lista_lugares_pertenecientes = []
        mi_lista_provincias_pertenecientes = []
        mi_lista_ciudades_pertenecientes = []
        mi_lista_barrios_pertenecientes = []

        for provincia in lista_provincias:
            if str(provincia.pais_perteneciente) == str(self.codigo):
                mi_lista_provincias_pertenecientes.append(provincia)
                for ciudad in lista_ciudades:
                    if str(ciudad.provincia_perteneciente) == str(provincia.codigo):
                        mi_lista_ciudades_pertenecientes.append(ciudad)
                        for barrio in lista_barrios:
                            print(barrio.ciudad_perteneciente)
                            if str(barrio.ciudad_perteneciente) == str(ciudad.codigo):
                                mi_lista_barrios_pertenecientes.append(barrio)

        mi_lista_lugares_pertenecientes.append(mi_lista_provincias_pertenecientes)
        mi_lista_lugares_pertenecientes.append(mi_lista_ciudades_pertenecientes)
        mi_lista_lugares_pertenecientes.append(mi_lista_barrios_pertenecientes)

        return mi_lista_lugares_pertenecientes


    def eliminar(self , mis_lugares_a_eliminar):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        mis_lugares_a_eliminar_2 = []
        mis_lugares_a_eliminar_2.append(mis_lugares_a_eliminar[1])
        mis_lugares_a_eliminar_2.append(mis_lugares_a_eliminar[2])

        for provincia in mis_lugares_a_eliminar[0]:
            provincia.eliminar(mis_lugares_a_eliminar_2)

        cursor.execute(
            "select coordenada_codigo from pais_has_coordenada where pais_codigo = '" + str(self.codigo) + "'")
        codigos = cursor.fetchall()

        for codigo in codigos:
            cursor.execute("delete from pais_has_coordenada where pais_codigo = '" + str(self.codigo) + "'")
            cursor.execute("delete from coordenada where codigo = '" + str(codigo[0]) + "'")

        cursor.execute("delete from pais where codigo = '" + str(self.codigo) + "'")

    def eliminar_coordenada(self, codigo_coordenada):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        cursor.execute("delete from pais_has_coordenada where coordenada_codigo = '" +
                       str(codigo_coordenada) + "'")
        cursor.execute("delete from coordenada where codigo = '" +
                       str(codigo_coordenada) + "'")

    def actualizar_nombre (self , nombre):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        cursor.execute("update pais set nombre = '" +str(nombre) + "' where codigo = '" + str(self.codigo) + "'")