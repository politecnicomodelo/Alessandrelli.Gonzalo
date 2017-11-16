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
    mi_pais.continente_perteneciente = item[2]
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
    mi_provincia.pais_perteneciente = item[2]
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
    mi_ciudad.provincia_perteneciente = item[2]
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
    mi_barrio.poblacion = item[2]
    mi_barrio.ciudad_perteneciente = item[3]
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



def eliminar_continente(continente , mis_lugares_a_eliminar):
    continente.eliminar(mis_lugares_a_eliminar)

    for barrio in mis_lugares_a_eliminar[3]:
        for item in lista_barrios:
            if item.codigo == barrio.codigo:
                lista_barrios.remove(item)
    for ciudad in mis_lugares_a_eliminar[2]:
        for item in lista_ciudades:
            if item.codigo == ciudad.codigo:
                lista_ciudades.remove(item)
    for provincia in mis_lugares_a_eliminar[1]:
        for item in lista_provincias:
            if item.codigo == provincia.codigo:
                lista_provincias.remove(item)
    for pais in mis_lugares_a_eliminar[0]:
        for item in lista_paises:
            if item.codigo == pais.codigo:
                lista_paises.remove(item)

    for item in lista_continentes:
        if item.codigo == continente.codigo:
            lista_continentes.remove(item)

def eliminar_pais(pais , mis_lugares_a_eliminar):
    pais.eliminar(mis_lugares_a_eliminar)

    for barrio in mis_lugares_a_eliminar[2]:
        for item in lista_barrios:
            if item.codigo == barrio.codigo:
                lista_barrios.remove(item)
    for ciudad in mis_lugares_a_eliminar[1]:
        for item in lista_ciudades:
            if item.codigo == ciudad.codigo:
                lista_ciudades.remove(item)
    for provincia in mis_lugares_a_eliminar[0]:
        for item in lista_provincias:
            if item.codigo == provincia.codigo:
                lista_provincias.remove(item)

    for item in lista_paises:
        if item.codigo == continente.codigo:
            lista_paises.remove(item)

def eliminar_provincia(provincia , mis_lugares_a_eliminar):
    provincia.eliminar(mis_lugares_a_eliminar)

    for barrio in mis_lugares_a_eliminar[1]:
        for item in lista_barrios:
            if item.codigo == barrio.codigo:
                lista_barrios.remove(item)
    for ciudad in mis_lugares_a_eliminar[0]:
        for item in lista_ciudades:
            if item.codigo == ciudad.codigo:
                lista_ciudades.remove(item)

    for item in lista_provincias:
        if item.codigo == provincia.codigo:
            lista_provincias.remove(item)

def eliminar_ciudad(ciudad , mis_lugares_a_eliminar):
    ciudad.eliminar(mis_lugares_a_eliminar)

    for barrio in mis_lugares_a_eliminar[0]:
        for item in lista_barrios:
            if item.codigo == barrio.codigo:
                lista_barrios.remove(item)

    for item in lista_ciudades:
        if item.codigo == ciudad.codigo:
            lista_ciudades.remove(item)

def eliminar_barrio(barrio):
    barrio.eliminar_objetos_relacionados()

    for item in lista_barrios:
        if item.codigo == barrio.codigo:
            lista_barrios.remove(item)

def eliminar_coordenada_barrio(barrio , codigo_coordenada):
    barrio.eliminar_coordenada(codigo_coordenada)

    for coordenada in barrio.coordenadas:
        if str(coordenada.codigo) == codigo_coordenada:
            barrio.coordenadas.remove(coordenada)

def eliminar_coordenada_ciudad(ciudad , codigo_coordenada):
    ciudad.eliminar_coordenada(codigo_coordenada)

    for coordenada in ciudad.coordenadas:
        if str(coordenada.codigo) == codigo_coordenada:
            ciudad.coordenadas.remove(coordenada)


def eliminar_coordenada_provincia(provincia , codigo_coordenada):
    provincia.eliminar_coordenada(codigo_coordenada)

    for coordenada in provincia.coordenadas:
        if str(coordenada.codigo) == codigo_coordenada:
            provincia.coordenadas.remove(coordenada)

def eliminar_coordenada_pais(pais , codigo_coordenada):
    pais.eliminar_coordenada(codigo_coordenada)

    for coordenada in pais.coordenadas:
        if str(coordenada.codigo) == codigo_coordenada:
            continente.coordenadas.remove(coordenada)

def eliminar_coordenada_continente(continente , codigo_coordenada):
    continente.eliminar_coordenada(codigo_coordenada)

    for coordenada in continente.coordenadas:
        if str(coordenada.codigo) == codigo_coordenada:
            continente.coordenadas.remove(coordenada)

def cambiar_nombre_barrio(barrio , nombre):

    for item in lista_barrios:
        if item == barrio:
            item.nombre = nombre
            item.actualzar_nombre(nombre)

def cambiar_nombre_ciudad(ciudad , nombre):

    for item in lista_ciudades:
        if item == ciudad:
            item.nombre = nombre
            item.actualzar_nombre(nombre)

def cambiar_nombre_provincia(provincia , nombre):

    for item in lista_provincias:
        if item == provincia:
            item.nombre = nombre
            item.actualzar_nombre(nombre)

def cambiar_nombre_pais(pais , nombre):

    for item in lista_paises:
        if item == pais:
            item.nombre = nombre
            item.actualzar_nombre(nombre)

def cambiar_nombre_continente(continente , nombre):

    for item in lista_barrios:
        if item == barrio:
            item.nombre = nombre
            item.actualzar_nombre(nombre)



def main ():
    while (True):
       selector = input("INGRESE UNA ACCION (0/1/2/3/4): \n\n<0>ABRIR CREAR\n<1>ABRIR MODIFICAR\n<2>ABRIR ELIMINAR\n"
                         "<3>ABRIR OBTENER\n\n<4>CERRAR PROGRAMA\n\nRESPUESTA: ")


       if (selector == "0"):
           selector = input("INGRESE UNA ACCION (0/1/2/3/4): \n\n<0> CREAR CONTINENTE\n<1> CREAR PAIS\n<2> CREAR PROVINCIA\n"
                            "<3> CREAR CIUDAD\n<4>CREAR BARRIO\n<5> IR AL MENU PRINCIPAL\n\nRESPUESTA: ")

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

           elif selector == "5":
               pass



       elif selector == "1":
           os.system('cls')
           selector = input(
               "INGRESE UNA ACCION (0/1/2/3/4/5): \n\n<0> ACTUALIZAR CONTINENTE\n<1> ACTUALIZAR PAIS \n<2> ACTUALIZAR PROVINCIA\n"
               "<3> ACTUALIZAR CIUDAD\n<4> ACTUALIZAR BARRIO\n<5> IR AL MENU PRINCIPAL\n\nRESPUESTA: ")

           if selector == "0":
               print("CONTINENTES:")

               for continente in lista_continentes:
                   print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

               codigo_continente = input("INGRESAR CODIGO CONTINENTE: ")

               selector = input(
                   "INGRESE UNA ACCION (0): \n\n<0> ACTUALIZAR NOMBRE\n\nRESPUESTA: ")

               if (selector == "0"):



           if selector == "1":
               pass

           if selector == "2":
               pass

           if selector == "3":
               pass

           if selector == "5":
               pass





       elif selector == "2":
           os.system('cls')
           selector = input("INGRESE UNA ACCION (0/1/2/3/4/5): \n\n<0> ELIMINAR CONTINENTE\n<1> ELIMINAR PAIS\n<2> ELIMINAR PROVINCIA\n"
                            "<3> ELIMINAR CIUDAD\n<4> ELIMINAR BARRIO\n<5> ELIMINAR COORDENADA\n<6> IR AL MENU PRINCIPAL\n\nRESPUESTA: ")

           mis_lugares_a_eliminar = []

           if selector == "0":
               print("CONTINENTES:")

               for item in lista_continentes:
                   print("CODIGO: " + str(item.codigo) + "\nNOMBRE: " + item.nombre + "\n")

               mi_continente = input("INGRESAR CODIGO CONTINENTE: ")
               for item in lista_continentes:
                    if str(item.codigo) == mi_continente:
                        continente = item
                        mis_lugares_a_eliminar = item.objetos_a_eliminar(lista_paises , lista_provincias , lista_ciudades , lista_barrios)

               print("LOS LUGARES QUE SE ELIMINARAN SON LOS SIGUIENTES:\n")
               for pais in mis_lugares_a_eliminar[0]:
                   print("NOMBRE: " + pais.nombre + "\nCODIGO PAIS: " + str(pais.codigo) + "\n")
                   print("PROVINCIAS DE: " + str(pais.codigo))
                   for provincia in mis_lugares_a_eliminar[1]:
                       if provincia.pais_perteneciente == pais.codigo:
                           print("NOMBRE: " + provincia.nombre + "\nCODIGO PROVINCIA: " + str(provincia.codigo) + "\n")
                           print("CIUDADES DE: " + str(provincia.codigo))
                           for ciudad in mis_lugares_a_eliminar[2]:
                               if ciudad.provincia_perteneciente == provincia.codigo:
                                   print("NOMBRE: " + ciudad.nombre + "\nCODIGO CIUDAD: " + str(ciudad.codigo) + "\n")
                                   print("BARRIOS DE: " + str(ciudad.codigo))
                                   for barrio in mis_lugares_a_eliminar[3]:
                                       if barrio.ciudad_perteneciente == ciudad.codigo:
                                           print("NOMBRE: " + barrio.nombre + "\nCODIGO BARRIO: " + str(barrio.codigo) + "\n")

               while (True):
                   respuesta = input("\n¿DESEA ELIMINAR ELIMINAR EL CONTINENTE JUNTO CON SUS RELACIONADOS? <S/N>\n\nRESPUESTA: ")
                   if ((respuesta == "s") or (respuesta == "S")):
                       eliminar_continente(continente , mis_lugares_a_eliminar)
                       break

                   elif ((respuesta == "n") or (respuesta == "N")):
                       os.system('cls')
                       break
                   else:
                       os.system('cls')
                       print("LETRA ERRONEA. REINGRESAR")



           elif selector == "1":
               print("CONTINENTES:")

               for continente in lista_continentes:
                   print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

               codigo_continente = input("INGRESAR CODIGO CONTINENTE QUE CONTIENE EL PAIS: ")

               print("PAISES:")

               for pais in lista_paises:
                   if str(pais.continente_perteneciente) == codigo_continente:

                       print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                       codigo_pais = input("INGRESAR CODIGO PAIS: ")

               for pais in lista_paises:
                   if str(pais.codigo) == codigo_pais:
                       mi_pais = pais
                       mis_lugares_a_eliminar = pais.objetos_a_eliminar(lista_provincias, lista_ciudades,
                                                                        lista_barrios)

               print("LOS LUGARES QUE SE ELIMINARAN SON LOS SIGUIENTES:\n")
               for provincia in mis_lugares_a_eliminar[0]:
                   if provincia.pais_perteneciente == mi_pais.codigo:
                       print("NOMBRE: " + provincia.nombre + "\nCODIGO PROVINCIA: " + str(provincia.codigo) + "\n")
                       print("CIUDADES DE: " + str(provincia.codigo))
                       for ciudad in mis_lugares_a_eliminar[1]:
                           if ciudad.provincia_perteneciente == provincia.codigo:
                               print("NOMBRE: " + ciudad.nombre + "\nCODIGO CIUDAD: " + str(ciudad.codigo) + "\n")
                               print("BARRIOS DE: " + str(ciudad.codigo))
                               for barrio in mis_lugares_a_eliminar[2]:
                                   if barrio.ciudad_perteneciente == ciudad.codigo:
                                       print("NOMBRE: " + barrio.nombre + "\nCODIGO BARRIO: " + str(
                                           barrio.codigo) + "\n")

               while (True):
                   respuesta = input(
                       "\n¿DESEA ELIMINAR ELIMINAR EL PAIS JUNTO CON SUS RELACIONADOS? <S/N>\n\nRESPUESTA: ")
                   if ((respuesta == "s") or (respuesta == "S")):
                       eliminar_pais(mi_pais, mis_lugares_a_eliminar)
                       break

                   elif ((respuesta == "n") or (respuesta == "N")):
                       os.system('cls')
                       break
                   else:
                       os.system('cls')
                       print("LETRA ERRONEA. REINGRESAR")



           elif selector == "2":
               print("CONTINENTES:")

               for continente in lista_continentes:
                   print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

               codigo_continente = input("INGRESAR CODIGO CONTINENTE LA PROVINCIA: ")

               print("PAISES:")

               for pais in lista_paises:
                   if str(pais.continente_perteneciente) == codigo_continente:
                       print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                       codigo_pais = input("INGRESAR CODIGO PAIS: ")

               for provincia in lista_provincias:
                   if str(provincia.pais_perteneciente) == codigo_pais:
                       print("CODIGO: " + str(provincia.codigo) + "\nNOMBRE: " + provincia.nombre + "\n")

                       codigo_provincia = input("INGRESAR CODIGO PROVINCIA: ")

               for provincia in lista_provincias:
                   if str(provincia.codigo) == codigo_provincia:
                       mi_provincia = provincia
                       mis_lugares_a_eliminar = provincia.objetos_a_eliminar(lista_ciudades , lista_barrios)

               print("LOS LUGARES QUE SE ELIMINARAN SON LOS SIGUIENTES:\n")
               for ciudad in mis_lugares_a_eliminar[0]:
                   if ciudad.provincia_perteneciente == provincia.codigo:
                       print("NOMBRE: " + ciudad.nombre + "\nCODIGO CIUDAD: " + str(ciudad.codigo) + "\n")
                       print("BARRIOS DE: " + str(ciudad.codigo))
                       for barrio in mis_lugares_a_eliminar[1]:
                           if barrio.ciudad_perteneciente == ciudad.codigo:
                               print("NOMBRE: " + barrio.nombre + "\nCODIGO BARRIO: " + str(
                                   barrio.codigo) + "\n")

               while (True):
                   respuesta = input(
                       "\n¿DESEA ELIMINAR ELIMINAR LA PROVINCIA JUNTO CON SUS RELACIONADOS? <S/N>\n\nRESPUESTA: ")
                   if ((respuesta == "s") or (respuesta == "S")):
                       eliminar_provincia(mi_provincia, mis_lugares_a_eliminar)
                       break

                   elif ((respuesta == "n") or (respuesta == "N")):
                       os.system('cls')
                       break
                   else:
                       os.system('cls')
                       print("LETRA ERRONEA. REINGRESAR")


           elif selector == "3":
               print("CONTINENTES:")

               for continente in lista_continentes:
                   print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

               codigo_continente = input("INGRESAR CODIGO CONTINENTE QUE CONTIENE LA CIUDAD: ")

               print("PAISES:")

               for pais in lista_paises:
                   if str(pais.continente_perteneciente) == codigo_continente:
                       print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                       codigo_pais = input("INGRESAR CODIGO PAIS QUE CONTIENE LA CIUDAD: ")

               print("PROVINCIAS:")

               for provincia in lista_provincias:
                   if str(provincia.pais_perteneciente) == codigo_pais:
                       print("CODIGO: " + str(provincia.codigo) + "\nNOMBRE: " + provincia.nombre + "\n")

                       codigo_provincia = input("INGRESAR CODIGO PROVINCIA QUE CONTIENE LA CIUDAD: ")

               for ciudad in lista_ciudades:
                   if str(ciudad.provincia_perteneciente) == codigo_provincia:
                       print("CODIGO: " + str(ciudad.codigo) + "\nNOMBRE: " + ciudad.nombre + "\n")

                       codigo_ciudad = input("INGRESAR CODIGO CIUDAD: ")

               for ciudad in lista_ciudades:
                   if str(ciudad.codigo) == codigo_ciudad:
                       mi_ciudad = ciudad
                       mis_lugares_a_eliminar = ciudad.objetos_a_eliminar(lista_barrios)

               print("LOS LUGARES QUE SE ELIMINARAN SON LOS SIGUIENTES:\n")
               for barrio in mis_lugares_a_eliminar[0]:
                   if barrio.ciudad_perteneciente == ciudad.codigo:
                       print("NOMBRE: " + barrio.nombre + "\nCODIGO BARRIO: " + str(
                           barrio.codigo) + "\n")

               while (True):
                   respuesta = input(
                       "\n¿DESEA ELIMINAR ELIMINAR LA CIUDAD JUNTO CON SUS RELACIONADOS? <S/N>\n\nRESPUESTA: ")
                   if ((respuesta == "s") or (respuesta == "S")):
                       eliminar_ciudad(mi_ciudad, mis_lugares_a_eliminar)
                       break

                   elif ((respuesta == "n") or (respuesta == "N")):
                       os.system('cls')
                       break
                   else:
                       os.system('cls')
                       print("LETRA ERRONEA. REINGRESAR")


           elif selector == "4":
               print("CONTINENTES:")

               for continente in lista_continentes:
                   print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

               codigo_continente = input("INGRESAR CODIGO CONTINENTE QUE CONTIENE EL BARRIO: ")

               print("PAISES:")

               for pais in lista_paises:
                   if str(pais.continente_perteneciente) == codigo_continente:
                       print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                       codigo_pais = input("INGRESAR CODIGO PAIS QUE CONTIENE EL BARRIO: ")

               print("PROVINCIAS:")

               for provincia in lista_provincias:
                   if str(provincia.pais_perteneciente) == codigo_pais:
                       print("CODIGO: " + str(provincia.codigo) + "\nNOMBRE: " + provincia.nombre + "\n")

                       codigo_provincia = input("INGRESAR CODIGO PROVINCIA QUE CONTIENE EL BARRIO: ")

               for ciudad in lista_ciudades:
                   if str(ciudad.provincia_perteneciente) == codigo_provincia:
                       print("CODIGO: " + str(ciudad.codigo) + "\nNOMBRE: " + ciudad.nombre + "\n")

                       codigo_ciudad = input("INGRESAR CODIGO CIUDAD QUE CONTIENE EL BARRIO: ")

               for barrio in lista_barrios:
                   if str(barrio.ciudad_perteneciente) == codigo_ciudad:
                       print("CODIGO: " + str(barrio.codigo) + "\nNOMBRE: " + barrio.nombre + "\n")

                       codigo_barrio = input("INGRESAR CODIGO BARRIO: ")

               for barrio in lista_barrios:
                   if str(barrio.codigo) == codigo_barrio:
                       mi_barrio = barrio

               while (True):
                   respuesta = input(
                       "\n¿DESEA ELIMINAR ELIMINAR EL BARRIO? <S/N>\n\nRESPUESTA: ")
                   if ((respuesta == "s") or (respuesta == "S")):
                       eliminar_barrio(mi_barrio)
                       break

                   elif ((respuesta == "n") or (respuesta == "N")):
                       os.system('cls')
                       break
                   else:
                       os.system('cls')
                       print("LETRA ERRONEA. REINGRESAR")

           elif selector == "5":
               selector = input("SELECCIONAR UN LUGAR (0/1/2/3/4/5)\n\n<0> CONTINENTE\n<1> PAIS\n<2> PROVINCIA\n"
                                "<3> CIUDAD\n<4> BARRIO\n<5> IR AL MENU PRINCIPAL\n\nRESPUESTA: ")

               if selector == "0":
                   print("CONTINENTES:")

                   for continente in lista_continentes:
                       print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

                   codigo_continente = input("INGRESAR CODIGO CONTINENTE A ELIMINAR COORDENADA: ")

                   for continente in lista_continentes:
                       if str(continente.codigo) == codigo_continente:
                           for coordenada in continente.coordenadas:
                               print("CODIGO: " + str(coordenada.codigo) + "\nLATITUD: " + str(coordenada.latitud)
                                     + "\nLONGITUD: " + str(coordenada.longitud) + "\n")

                           codigo_coordenada = input("INGRESAR CODIGO COORDENADA: ")

                           eliminar_coordenada_continente(continente , codigo_coordenada)

               if selector == "1":
                   print("CONTINENTES:")

                   for continente in lista_continentes:
                       print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

                   codigo_continente = input("INGRESAR CODIGO CONTINENTE QUE CONTIENE PAIS A ELIMINAR COORDENADA: ")

                   for pais in lista_paises:
                       if str(pais.continente_perteneciente) == codigo_continente:
                           for coordenada in pais.coordenadas:
                               print("CODIGO: " + str(coordenada.codigo) + "\nLATITUD: " + str(coordenada.latitud)
                                     + "\nLONGITUD: " + str(coordenada.longitud) + "\n")

                           codigo_coordenada = input("INGRESAR CODIGO COORDENADA: ")

                           cursor.execute("delete from pais_has_coordenada where coordenada_codigo = '" +
                                          str(codigo_coordenada) + "'")
                           cursor.execute("delete from coordenada where codigo = '" +
                                          str(codigo_coordenada) + "'")

                           for coordenada in pais.coordenadas:
                               if str(coordenada.codigo) == codigo_coordenada:
                                   pais.coordenadas.remove(coordenada)

               elif selector == "2":
                   print("CONTINENTES:")

                   for continente in lista_continentes:
                       print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

                   codigo_continente = input("INGRESAR CODIGO CONTINENTE QUE CONTIENE PROVINCIA A ELIMINAR COORDENADA: ")

                   for pais in lista_paises:
                       if str(pais.continente_perteneciente) == codigo_continente:
                           print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                   codigo_pais = input("INGRESAR CODIGO PAIS QUE CONTIENE PROVINCIA A ELIMINAR COORDENADA: ")

                   for provincia in lista_provincias:
                       if str(provincia.pais_perteneciente) == codigo_pais:
                           for coordenada in provincia.coordenadas:
                               print("CODIGO: " + str(coordenada.codigo) + "\nLATITUD: " + str(coordenada.latitud)
                                     + "\nLONGITUD: " + str(coordenada.longitud) + "\n")
                           codigo_coordenada = input("INGRESAR CODIGO COORDENADA: ")

                           eliminar_coordenada_provincia(provincia, codigo_coordenada)
                           break


               elif selector == "3":
                   print("CONTINENTES:")

                   for continente in lista_continentes:
                       print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

                   codigo_continente = input(
                       "INGRESAR CODIGO CONTINENTE QUE CONTIENE CIUDAD A ELIMINAR COORDENADA: ")

                   for pais in lista_paises:
                       if str(pais.continente_perteneciente) == codigo_continente:
                           print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                   codigo_pais = input("INGRESAR CODIGO PAIS QUE CONTIENE PROVINCIA A ELIMINAR COORDENADA: ")

                   for provincia in lista_provincias:
                       if str(provincia.pais_perteneciente) == codigo_pais:
                           print("CODIGO: " + str(provincia.codigo) + "\nNOMBRE: " + provincia.nombre + "\n")

                   codigo_provincia = input("INGRESAR CODIGO PROVINCIA QUE CONTIENE CIUDAD A ELIMINAR COORDENADA: ")

                   for ciudad in lista_ciudades:
                       if str(ciudad.provincia_perteneciente) == codigo_provincia:
                           for coordenada in ciudad.coordenadas:
                               print("CODIGO: " + str(coordenada.codigo) + "\nLATITUD: " + str(coordenada.latitud)
                                     + "\nLONGITUD: " + str(coordenada.longitud) + "\n")

                           codigo_coordenada = input("INGRESAR CODIGO COORDENADA: ")

                           eliminar_coordenada_ciudad(ciudad , codigo_coordenada)

               elif selector == "4":
                   print("CONTINENTES:")

                   for continente in lista_continentes:
                       print("CODIGO: " + str(continente.codigo) + "\nNOMBRE: " + continente.nombre + "\n")

                   codigo_continente = input(
                       "INGRESAR CODIGO CONTINENTE QUE CONTIENE BARRIO A ELIMINAR COORDENADA: ")

                   for pais in lista_paises:
                       if str(pais.continente_perteneciente) == codigo_continente:
                           print("CODIGO: " + str(pais.codigo) + "\nNOMBRE: " + pais.nombre + "\n")

                   codigo_pais = input("INGRESAR CODIGO PAIS QUE CONTIENE BARRIO A ELIMINAR COORDENADA: ")

                   for provincia in lista_provincias:
                       if str(provincia.pais_perteneciente) == codigo_pais:
                           print("CODIGO: " + str(provincia.codigo) + "\nNOMBRE: " + provincia.nombre + "\n")

                   codigo_provincia = input("INGRESAR CODIGO PROVINCIA QUE CONTIENE BARRIO A ELIMINAR COORDENADA: ")

                   for ciudad in lista_ciudades:
                       if str(ciudad.continente_perteneciente) == codigo_provincia:
                           print("CODIGO: " + str(ciudad.codigo) + "\nNOMBRE: " + ciudad.nombre + "\n")

                   codigo_ciudad = input("INGRESAR CODIGO CIUDAD QUE CONTIENE BARRIO A ELIMINAR COORDENADA: ")

                   for barrio in lista_barrios:
                       if str(barrio.ciudad_perteneciente) == codigo_ciudad:
                           for coordenada in barrio.coordenadas:
                               print("CODIGO: " + str(coordenada.codigo) + "\nLATITUD: " + str(coordenada.latitud)
                                     + "\nLONGITUD: " + str(coordenada.longitud) + "\n")

                           codigo_coordenada = input("INGRESAR CODIGO COORDENADA: ")

                           eliminar_coordenada_barrio(barrio , codigo_coordenada)
                           break


               elif selector == "5":
                   pass


           elif selector == "6":
               pass



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