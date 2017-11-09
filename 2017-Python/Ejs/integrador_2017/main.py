import pymysql
from clases.lugar import lugar
from clases.continente import continente
from clases.pais import pais
from clases.provincia import provincia
from clases.ciudad import ciudad
from clases.barrio import barrio
from clases.coordenada import coordenada

db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
                      db = "mydb" , autocommit = True)
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


def crear_barrio (nombre , poblacion):
    mi_barrio = barrio()

    cursor.execute("insert into barrio values (NULL , nombre , provincia_perteneciente)")