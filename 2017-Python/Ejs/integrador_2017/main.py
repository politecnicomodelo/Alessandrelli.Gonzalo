import pymysql
from clases.Lugar import lugar
from clases.Continente import continente
from clases.Pais import pais
from clases.Provincia import provincia
from clases.Ciudad import ciudad
from clases.Barrio import barrio
from clases.Coordenada import coordenada

db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" , db = "mydb" , autocommit = True)
cursor = db.cursor()


cursor.execute("select * from coordenada")
coordenadas = cursor.fetchall()
lista_coordenadas = []
lista_continentes = []
lista_paises = []
lista_provincias = []
lista_ciudades = []
lista_barrios = []

for item in coordenadas:
    mi_coordenada = coordenada()
    mi_coordenada.codigo = item[0]
    mi_coordenada.latitud = item[1]
    mi_coordenada.longitud = item[2]
    lista_coordenadas.append(mi_coordenada)

cursor.execute("select * from continente")
continentes = cursor.fetchall()
cursor.execute("select * from continente_has_coordenada")
continente_coordenadas = cursor.fetchall()

for item in continentes:
    mi_continente = continente()
    mi_continente.codigo = item[0]
    mi_continente.nombre = item[1]
    for coordenada in continente_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == coordenada[1]:
                mi_continente.coordenadas.append(item)
    lista_continentes.append(mi_continente)

cursor.execute("select * from pais")
paises = cursor.fetchall()
cursor.execute("select * from pais_has_coordenada")
pais_coordenadas = cursor.fetchall()

for item in paises:
    mi_pais = pais()
    mi_pais.codigo = item[0]
    mi_pais.nombre = item[1]
    for coordenada in pais_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == coordenada[1]:
                mi_pais.coordenadas.append(item)
    lista_paises.append(mi_pais)

cursor.execute("select * from provincia")
provincias = cursor.fetchall()
cursor.execute("select * from provincia_has_coordenada")
provincia_coordenadas = cursor.fetchall()

for item in provincias:
    mi_provincia = continente()
    mi_provincia.codigo = item[0]
    mi_provincia.nombre = item[1]
    for coordenada in provincia_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == coordenada[1]:
                mi_provincia.coordenadas.append(item)
    lista_provincias.append(mi_provincia)

cursor.execute("select * from ciudad")
ciudades = cursor.fetchall()
cursor.execute("select * from ciudad_has_coordenada")
ciudad_coordenadas = cursor.fetchall()

for item in ciudades:
    mi_ciudad = continente()
    mi_ciudad.codigo = item[0]
    mi_ciudad.nombre = item[1]
    for coordenada in ciudad_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == coordenada[1]:
                mi_ciudad.coordenadas.append(item)
    lista_ciudades.append(mi_ciudad)

cursor.execute("select * from barrio")
barrios = cursor.fetchall()
cursor.execute("select * from barrio_has_coordenada")
barrio_coordenadas = cursor.fetchall()

for item in barrios:
    mi_barrio = barrio()
    mi_barrio.codigo = item[0]
    mi_barrio.nombre = item[1]
    for coordenada in barrio_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == coordenada[1]:
                mi_barrio.coordenadas.append(item)
    lista_barrios.append(mi_barrio)






    def crear_coordenada():
        mi_coordenada = coordenada()

        mi_coordenada.latitud = input("INGRESAR LATITUD: ")
        mi_coordenada.longitud = input("INGRESAR LONGITUD: ")

        return mi_coordenada


def crear_barrio(mi_ciudad):
    nombre = input("NOMBRE DEL BARRIO: ")
    poblacion = input("POBLACION TOTAL: ")
    lista_coordenadas = []

    while (True):
        if input("¿AGREGAR UNA NUEVA COORDENADA? (0/1): ") == "0":
            break
        else:
            lista_coordenadas.append(crear_coordenada())

    return mi_ciudad.crear_barrio(nombre , poblacion , lista_coordenadas)


def crear_ciudad(mi_provincia):
    nombre = input("NOMBRE DE LA CIUDAD: ")
    lista_coordenadas = []

    while (True):
        if input("¿AGREGAR UNA NUEVA COORDENADA? (0/1): ") == "0":
            break
        else:
            lista_coordenadas.append(crear_coordenada())

        return mi_provincia.crear_ciudad(nombre , lista_coordenadas)


def crear_provincia(mi_pais):
    nombre = input("NOMBRE DE LA PROVINCIA: ")
    lista_coordenadas = []

    while (True):
        if input("¿AGREGAR UNA NUEVA COORDENADA? (0/1): ") == "0":
            break
        else:
            lista_coordenadas.append(crear_coordenada())

        return mi_pais.crear_provincia(nombre , lista_coordenadas)


def crear_pais(mi_continente):
    nombre = input("NOMBRE DEL BARRIO: ")
    lista_coordenadas = []

    while (True):
        if input("¿AGREGAR UNA NUEVA COORDENADA? (0/1): ") == "0":
            break
        else:
            lista_coordenadas.append(crear_coordenada())

        return mi_continente.crear_pais(nombre , lista_coordenadas)


def crear_continente(nombre , lista_coordenadas):
    mi_continente = continente()

    cursor.execute("insert into continente values (NULL , '" + str(nombre) + "')")
    codigo = cursor.lastrowid

    for item in lista_coordenadas:
        cursor.execute("insert into coordenada values (NULL , '" + str(item.latitud) + "' , '" + str(item.longitud) + "')")
        codigo_coordenada = cursor.lastrowid
        cursor.execute("insert into continente_has_coordenada values ('" + str(codigo) + "' ,"
                       " '" + str(codigo_coordenada) + "')")
        item.codigo = codigo_coordenada

    mi_continente.codigo = codigo
    mi_continente.nombre = nombre
    mi_continente.coordenadas = lista_coordenadas

    return mi_continente


def main ():
    while (True):
       selector = input("INGRESE UNA ACCION (0/1/2/3): \n\n<0> CREAR CONTINENTE\n<1> CREAR PAIS\n<2> CREAR PROVINCIA\n"
                        "<3> CREAR CIUDAD\n<4> CREAR BARRIO\n\nRESPUESTA: ")

       if selector == "0":
           nombre = input("NOMBRE DEL CONTINENTE: ")
           lista_coordenadas = []

           while (True):
               if input("¿AGREGAR UNA NUEVA COORDENADA? (0/1): ") == "0":
                   break
               else:
                   lista_coordenadas.append(crear_coordenada())

           lista_continentes.append(crear_continente(nombre, lista_coordenadas))



       elif selector == "1":
           print("CONTINENTES:")

           for item in lista_continentes:
               print("CODIGO: " + item.codigo + "\nNOMBRE: " + item.nombre)

           mi_continente = input("INGRESAR CODIGO CONTINENTE: ")

           lista_paises.append(crear_pais(mi_continente))


       elif selector == "2":
           print("PAISES:")

           for item in lista_paises:
               print("CODIGO: " + item.codigo + "\nNOMBRE: " + item.nombre)

           mi_pais = input("INGRESAR CODIGO PAIS: ")

           lista_ciudades.append(crear_ciudad(mi_pais))


       elif selector == "3":
           print("ciudades:")

           for item in lista_ciudades:
               print("CODIGO: " + item.codigo + "\nNOMBRE: " + item.nombre)

           mi_ciudad = input("INGRESAR CODIGO CIUDAD: ")

           lista_barrios.append(crear_barrio(mi_ciudad))

main()