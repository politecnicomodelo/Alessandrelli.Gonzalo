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


    def objetos_a_eliminar(self , lista_barrios):

        mi_lista_lugares_pertenecientes = []
        mi_lista_barrios_pertenecientes = []

        for barrio in lista_barrios:
            print(barrio.ciudad_perteneciente)
            if str(barrio.ciudad_perteneciente) == str(ciudad.codigo):
                mi_lista_barrios_pertenecientes.append(barrio)

        mi_lista_lugares_pertenecientes.append(mi_lista_barrios_pertenecientes)

        return mi_lista_lugares_pertenecientes



    def eliminar(self, mis_lugares_a_eliminar):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        for barrio in mis_lugares_a_eliminar[0]:
            barrio.eliminar_objetos_relacionados()

        cursor.execute("select coordenada_codigo from ciudad_has_coordenada where ciudad_codigo = '" + str(
            self.codigo) + "'")
        codigos = cursor.fetchall()
        for codigo in codigos:
            cursor.execute("delete from ciudad_has_coordenada where ciudad_codigo = '" + str(self.codigo) + "'")
            cursor.execute("delete from coordenada where codigo = '" + str(codigo[0]) + "'")

        cursor.execute("delete from ciudad where codigo = '" + str(self.codigo) + "'")

