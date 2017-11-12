import pymysql
import os
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
mis_coordenadas = cursor.fetchall()
lista_coordenadas = []
lista_continentes = []
lista_paises = []
lista_provincias = []
lista_ciudades = []
lista_barrios = []

for item in mis_coordenadas:
    Mi_coordenada = coordenada()
    Mi_coordenada.codigo = item[0]
    Mi_coordenada.latitud = item[1]
    Mi_coordenada.longitud = item[2]
    lista_coordenadas.append(Mi_coordenada)

cursor.execute("select * from continente")
continentes = cursor.fetchall()
cursor.execute("select * from continente_has_coordenada")
continente_coordenadas = cursor.fetchall()

for item in continentes:
    mi_continente = continente()
    mi_continente.codigo = item[0]
    mi_continente.nombre = item[1]
    for mi_coordenada in continente_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == mi_coordenada[1]:
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
    for mi_coordenada in pais_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == mi_coordenada[1]:
                mi_pais.coordenadas.append(item)
    lista_paises.append(mi_pais)

cursor.execute("select * from provincia")
provincias = cursor.fetchall()
cursor.execute("select * from provincia_has_coordenada")
provincia_coordenadas = cursor.fetchall()

for item in provincias:
    mi_provincia = provincia()
    mi_provincia.codigo = item[0]
    mi_provincia.nombre = item[1]
    for mi_coordenada in provincia_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == mi_coordenada[1]:
                mi_provincia.coordenadas.append(item)
    lista_provincias.append(mi_provincia)

cursor.execute("select * from ciudad")
ciudades = cursor.fetchall()
cursor.execute("select * from ciudad_has_coordenada")
ciudad_coordenadas = cursor.fetchall()

for item in ciudades:
    mi_ciudad = ciudad()
    mi_ciudad.codigo = item[0]
    mi_ciudad.nombre = item[1]
    for mi_coordenada in ciudad_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == mi_coordenada[1]:
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
    for mi_coordenada in barrio_coordenadas:
        for item in lista_coordenadas:
            if item.codigo == mi_coordenada[1]:
                mi_barrio.coordenadas.append(item)
    lista_barrios.append(mi_barrio)






def crear_coordenada():
    Coordenada = []

    Coordenada.append((input("INGRESAR LATITUD: ") , input("INGRESAR LONGITUD: ")))

    return Coordenada


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
    nombre = input("NOMBRE DEL PAIS: ")
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

    mi_continente.codigo = codigo
    mi_continente.nombre = nombre
    mi_continente.coordenadas = lista_coordenadas

    for item in lista_coordenadas:
        print(item)
        print(item[0])
        mi_continente.crear_coordenada(item[0][0], item[0][1], mi_continente)

    return mi_continente


def main ():
    while (True):
       selector = input("INGRESE UNA ACCION (0/1/2/3/4): \n\n<0>ABRIR CREAR\n<1>ABRIR MODIFICAR\n<2>ABRIR ELIMINAR\n"
                         "<3>ABRIR OBTENER\n<4>CERRAR PROGRAMA\n\nRESPUESTA: ")


       if (selector == "0"):
           selector = input("INGRESE UNA ACCION (0/1/2/3/4): \n\n<0> CREAR CONTINENTE\n<1> CREAR PAIS\n<2> CREAR PROVINCIA\n"
                            "<3> CREAR CIUDAD\n<4>CREAR BARRIO\n\nRESPUESTA: ")

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
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_continente = input("INGRESAR CODIGO CONTINENTE: ")
               for item in lista_continentes:
                    if str(item.codigo) == mi_continente:
                        mi_continente = item

               lista_paises.append(crear_pais(mi_continente))



           elif selector == "2":

               print("PAISES:")

               for item in lista_paises:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_pais = input("INGRESAR CODIGO PAIS: ")

               for item in lista_paises:

                   if str(item.codigo) == mi_pais:
                       mi_pais = item

               lista_provincias.append(crear_provincia(mi_pais))


           elif selector == "3":
               print("PROVINCIAS:")

               for item in lista_provincias:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_provincia = input("INGRESAR CODIGO PROVINCIA: ")
               for item in lista_provincias:
                   if str(item.codigo) == mi_provincia:
                       mi_provincia = item

               lista_ciudades.append(crear_ciudad(mi_provincia))


           elif selector == "4":
               print("CIUDADES:")

               for item in lista_ciudades:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_ciudad = input("INGRESAR CODIGO CIUDAD: ")
               for item in lista_ciudades:
                    if str(item.codigo) == mi_ciudad:
                        mi_ciudad = item

               lista_barrios.append(crear_barrio(mi_ciudad))



       elif selector == "1":
           os.system('cls')



       elif selector == "2":
           os.system('cls')
           selector = input("INGRESE UNA ACCION (0/1/2/3/4/5): \n\n<0> ELIMINAR CONTINENTE\n<1> ELIMINAR PAIS\n<2> ELIMINAR PROVINCIA\n"
                            "<3> ELIMINAR CIUDAD\n<4> ELIMINAR BARRIO\n<4> ELIMINAR COORDENADA\n\nRESPUESTA: ")

           if selector == "0": #aca

               print("CONTINENTES:")

               for item in lista_continentes:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_continente = input("INGRESAR CODIGO CONTINENTE: ")
               for item in lista_continentes:
                    if str(item.codigo) == mi_continente:
                        item.eliminar_continente

               lista_continentes.append(crear_continente(nombre, lista_coordenadas))



           elif selector == "1":
               print("CONTINENTES:")

               for item in lista_continentes:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_continente = input("INGRESAR CODIGO CONTINENTE: ")
               for item in lista_continentes:
                    if str(item.codigo) == mi_continente:
                        mi_continente = item

               lista_paises.append(crear_pais(mi_continente))



           elif selector == "2":

               print("PAISES:")

               for item in lista_paises:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_pais = input("INGRESAR CODIGO PAIS: ")

               for item in lista_paises:

                   if str(item.codigo) == mi_pais:
                       mi_pais = item

               lista_provincias.append(crear_provincia(mi_pais))


           elif selector == "3":
               print("PROVINCIAS:")

               for item in lista_provincias:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_provincia = input("INGRESAR CODIGO PROVINCIA: ")
               for item in lista_provincias:
                   if str(item.codigo) == mi_provincia:
                       mi_provincia = item

               lista_ciudades.append(crear_ciudad(mi_provincia))


           elif selector == "4":
               print("CIUDADES:")

               for item in lista_ciudades:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_ciudad = input("INGRESAR CODIGO CIUDAD: ")
               for item in lista_ciudades:
                    if str(item.codigo) == mi_ciudad:
                        mi_ciudad = item

               lista_barrios.append(crear_barrio(mi_ciudad))



       elif selector == "3":
           os.system('cls')
           print("por hacer")



       elif selector == "4":
           os.system('cls')
           print("ADIOS")
           break

       else:
           os.system('cls')
           print("NUMERO ERRONEO. REINGRESAR")

       os.system('cls')

main()