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

    def objetos_a_eliminar (self , lista_paises , lista_provincias , lista_ciudades , lista_barrios):

        mi_lista_lugares_pertenecientes = []
        mi_lista_paises_pertenecientes = []
        mi_lista_provincias_pertenecientes = []
        mi_lista_ciudades_pertenecientes = []
        mi_lista_barrios_pertenecientes = []

        for pais in lista_paises:
            if str(pais.continente_perteneciente) == str(self.codigo):
                mi_lista_paises_pertenecientes.append(pais)
                for provincia in lista_provincias:
                    if str(provincia.pais_perteneciente) == str(pais.codigo):
                        mi_lista_provincias_pertenecientes.append(provincia)
                        for ciudad in lista_ciudades:
                            if str(ciudad.provincia_perteneciente) == str(provincia.codigo):
                                mi_lista_ciudades_pertenecientes.append(ciudad)
                                for barrio in lista_barrios:
                                    print(barrio.ciudad_perteneciente)
                                    if str(barrio.ciudad_perteneciente) == str(ciudad.codigo):
                                        mi_lista_barrios_pertenecientes.append(barrio)

        mi_lista_lugares_pertenecientes.append(mi_lista_paises_pertenecientes)
        mi_lista_lugares_pertenecientes.append(mi_lista_provincias_pertenecientes)
        mi_lista_lugares_pertenecientes.append(mi_lista_ciudades_pertenecientes)
        mi_lista_lugares_pertenecientes.append(mi_lista_barrios_pertenecientes)

        return mi_lista_lugares_pertenecientes

    def eliminar(self , mis_lugares_a_eliminar):
        db = pymysql.connect(host='127.0.0.1', user="root", password="", db="mydb", autocommit=True)
        cursor = db.cursor()

        for pais in mis_lugares_a_eliminar[0]:
            pais.eliminar(mis_lugares_a_eliminar[1 , 2 , 3])

        cursor.execute("select coordenada_codigo from continente_has_coordenada where continente_codigo = '" + str(self.codigo) + "'")
        codigo = cursor.fetchall()
        codigo = codigo[0]
        cursor.execute("delete from continente_has_coordenada where continente_codigo = '" + str(self.codigo) + "'")
        cursor.execute("delete from coordenada where codigo = '" + str(codigo) + "'")
        cursor.execute("delete from continente where codigo = '" + str(self.codigo) + "'")


