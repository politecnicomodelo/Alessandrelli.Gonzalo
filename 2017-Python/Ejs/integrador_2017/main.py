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


def agregar_coordenada (latitud , longitud , mi_lugar):
    cursor.execute("insert into coordenada values (NULL , '"+str(latitud)+"' , '"+str(longitud)+"')")
    codigo = cursor.lastrowid
    print(str(mi_lugar.codigo))
    if mi_lugar.soy() == "barrio":
        cursor.execute("insert into barrio_has_coordenada values ('"+str(mi_barrio.codigo)+"' , '"+str(codigo)+"')")
    elif mi_lugar.soy() == "ciudad":
        cursor.execute("insert into ciudad_has_coordenada values ('"+str(mi_ciudad.codigo)+"' , '"+str(codigo)+"')")
    elif mi_lugar.soy() == "provincia":
        cursor.execute("insert into provincia_has_coordenada values ('"+str(mi_provincia.codigo)+"' , '"+str(codigo)+"')")
    elif mi_lugar.soy() == "pais":
        cursor.execute("insert into pais_has_coordenada values ('"+str(mi_pais.codigo)+"' , '"+str(codigo)+"')")
    else:
        cursor.execute("insert into continente_has_coordenada values ('"+str(mi_continente.codigo)+"' , '"+str(codigo)+"')")

    mi_coordenada = coordenada()
    mi_coordenada.codigo = codigo
    mi_coordenada.latitud = latitud
    mi_coordenada.longitud = longitud
    mi_lugar.coordenadas.append(mi_coordenada)

    return mi_lugar


def crear_barrio (nombre , poblacion , ciudad_perteneciente , lista_barrios):
    mi_barrio = barrio()

    cursor.execute("select * from ciudad where nombre = '"+str(ciudad_perteneciente)+"'")
    ciudad = cursor.fetchall()
    if ciudad == ():
        return 0 , "no existe la ciudad " + ciudad_perteneciente;
    else:
        print("CIUDADES CON ESE NOMBRE: ")
        for item in ciudad:
            print("CODIGO: " + str(item[0]))
            print("NOMBRE: " + item[1])
            print("PROVINCIA CODIGO: " + str(item[2]) + "\n\n")
        codigo = input("INGRESAR UN CODIGO MOSTRADO: ")
        for item in ciudad:
            if str(item[0]) == codigo:
                cursor.execute(
                    "insert into barrio values (NULL , '" + str(nombre) + "' , '" + str(poblacion) + "' , '" + str(
                        codigo) + "')")
                codigo = cursor.lastrowid

                mi_barrio.codigo = codigo
                mi_barrio.nombre = nombre
                mi_barrio.poblacion = poblacion

                while (True):
                    if input("¿AGREGAR UNA NUEVA COORDENADA? (0/1): ") == "0":
                        break
                    else:
                        mi_barrio = agregar_coordenada(input("LATITUD: ") , input("LONGITUD: ") , mi_barrio)

                lista_barrios.append(mi_barrio)
                return 1 , lista_barrios

        return 0, "codigo ingresado erroneo"


def crear_ciudad (nombre , provincia_perteneciente , lista_ciudades):
    mi_ciudad = ciudad()

    cursor.execute("select * from provincia where nombre = '"+str(provincia_perteneciente)+"'")
    provincia = cursor.fetchall()
    if provincia == ():
        return 0 , "no existe la provincia " + provincia_perteneciente;
    else:
        print("PROVINCIAS CON ESE NOMBRE: ")
        for item in provincia:
            print("CODIGO: " + str(item[0]))
            print("NOMBRE: " + item[1])
            print("PROVINCIA CODIGO: " + str(item[2]) + "\n\n")
        codigo = input("INGRESAR UN CODIGO MOSTRADO: ")
        for item in provincia:
            if str(item[0]) == codigo:
                cursor.execute(
                    "insert into ciudad values (NULL , '" + str(nombre) + "' , '" + str(
                        codigo) + "')")
                codigo = cursor.lastrowid

                #obtener coodenadas con funcion todavia sin hacer aca

                mi_ciudad.codigo = codigo
                mi_ciudad.nombre = nombre
                lista_ciudades.append(mi_ciudad)
                return 1 , lista_ciudades

        return 0 , "codigo ingresado erroneo"


def crear_provincia (nombre , pais_perteneciente , lista_provincias):
    mi_provincia = provincia()

    cursor.execute("select * from pais where nombre = '"+str(pais_perteneciente)+"'")
    pais = cursor.fetchall()
    if pais == ():
        return 0 , "no existe el pais " + pais_perteneciente;
    else:
        print("PAISES CON ESE NOMBRE: ")
        for item in pais:
            print("CODIGO: " + str(item[0]))
            print("NOMBRE: " + item[1])
            print("PAIS CODIGO: " + str(item[2]) + "\n\n")
        codigo = input("INGRESAR UN CODIGO MOSTRADO: ")
        for item in pais:
            if str(item[0]) == codigo:
                cursor.execute(
                    "insert into provincia values (NULL , '" + str(nombre) + "' , '" + str(
                        codigo) + "')")
                codigo = cursor.lastrowid

                #obtener coodenadas con funcion todavia sin hacer aca

                mi_provincia.codigo = codigo
                mi_provincia.nombre = nombre
                lista_provincias.append(mi_provincia)
                return 1 , lista_provincias
        return 0, "codigo ingresado erroneo"


def crear_pais (nombre , continente_perteneciente , lista_paises):
    mi_pais = pais()

    cursor.execute("select * from continente where nombre = '"+str(continente_perteneciente)+"'")
    continente = cursor.fetchall()
    if continente == ():
        return 0 , "no existe el continente " + continente_perteneciente;
    else:
        print("CONTINENTES CON ESE NOMBRE: ")
        for item in pais:
            print("CODIGO: " + str(item[0]))
            print("NOMBRE: " + item[1])
            print("CONTINENTE CODIGO: " + str(item[2]) + "\n\n")
        codigo = input("INGRESAR UN CODIGO MOSTRADO: ")
        for item in continente:
            if str(item[0]) == codigo:
                cursor.execute(
                    "insert into pais values (NULL , '" + str(nombre) + "' , '" + str(
                        codigo) + "')")
                codigo = cursor.lastrowid

                #obtener coodenadas con funcion todavia sin hacer aca

                mi_pais.codigo = codigo
                mi_pais.nombre = nombre
                lista_paises.append(mi_pais)
                return 1 , lista_paises

        return 0, "codigo ingresado erroneo"


def crear_continente (nombre , lista_continentes):
    mi_continente = continente()

    cursor.execute("insert into continente values (NULL , '"+str(nombre)+"')")

    codigo = cursor.lastrowid

    #obtener coodenadas con funcion todavia sin hacer aca

    mi_continente.codigo = codigo
    mi_continente.nombre = nombre
    lista_continentes.append(mi_continente)
    return 1 , lista_continentes


def eliminar_barrio (nombre , lista_barrios):
    cursor.execute("delete from barrio where nombre == ")


print(crear_barrio("saavedra" , 15000 , "buenos aires" , lista_barrios))