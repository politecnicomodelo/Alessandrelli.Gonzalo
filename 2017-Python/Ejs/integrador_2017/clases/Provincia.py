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

    def objetos_a_eliminar(self , lista_ciudades, lista_barrios):

        mi_lista_lugares_pertenecientes = []
        mi_lista_ciudades_pertenecientes = []
        mi_lista_barrios_pertenecientes = []

        for ciudad in lista_ciudades:
            if str(ciudad.provincia_perteneciente) == str(self.codigo):
                mi_lista_ciudades_pertenecientes.append(ciudad)
                for barrio in lista_barrios:
                    print(barrio.ciudad_perteneciente)
                    if str(barrio.ciudad_perteneciente) == str(ciudad.codigo):
                        mi_lista_barrios_pertenecientes.append(barrio)

        mi_lista_lugares_pertenecientes.append(mi_lista_ciudades_pertenecientes)
        mi_lista_lugares_pertenecientes.append(mi_lista_barrios_pertenecientes)

        return mi_lista_lugares_pertenecientes



    def eliminar(self, mis_lugares_a_eliminar):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        for ciudad in mis_lugares_a_eliminar[0]:
            ciudad.eliminar(mis_lugares_a_eliminar[1])

        cursor.execute("select coordenada_codigo from provincia_has_coordenada where provincia_codigo = '" + str(
            self.codigo) + "'")
        codigo = cursor.fetchall()
        codigo = codigo[0]
        cursor.execute("delete from provincia_has_coordenada where provincia_codigo = '" + str(self.codigo) + "'")
        cursor.execute("delete from coordenada where codigo = '" + str(codigo) + "'")
        cursor.execute("delete from provincia where codigo = '" + str(self.codigo) + "'")