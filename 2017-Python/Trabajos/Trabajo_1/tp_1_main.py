from datetime import date
from datetime import datetime
from clases.tripulacion import tripulacion
from clases.piloto import piloto
from clases.servicio import servicio
from clases.pasajero import pasajero
from clases.aviones import aviones
from clases.vuelos import vuelos
import sys

lista_personas = []
lista_aviones = []
lista_vuelos = []

mi_pasajero = pasajero()
mi_piloto = piloto()
mi_tripulante_servicio = servicio()
mi_avion = aviones()
mi_vuelo = vuelos()

dato = []
dato2 = []

arc_personas = open("personas.dat", "r")
for line in arc_personas:
        dato = line.split('|')
        if (dato [0] == "Pasajero"):
            mi_pasajero = pasajero()
            mi_pasajero.agregar_nombre(dato[1])
            mi_pasajero.agregar_apellido(dato[2])
            dato2 = dato[3].split("-")
            mi_pasajero.agregar_fecha_nacimiento(date (int(dato2[2]) ,int(dato2[1]) , int(dato2[0])))
            mi_pasajero.agregar_dni(dato[4])
            if (int(dato[5]) == 1):
                mi_pasajero.agregar_vip(True)
            else:
                mi_pasajero.agregar_vip(False)
            if dato[6] != "\n":
                mi_pasajero.agregar_necesidades_especiales(dato[6])
            else:
                mi_pasajero.agregar_necesidades_especiales(False)
            lista_personas.append(mi_pasajero)

        elif (dato [0] == "Piloto"):
            mi_piloto = piloto()
            mi_piloto.agregar_nombre(dato[1])
            mi_piloto.agregar_apellido(dato[2])
            dato2 = dato[3].split("-")
            mi_piloto.agregar_fecha_nacimiento(date (int(dato2[2]) ,int(dato2[1]) , int(dato2[0])))
            mi_piloto.agregar_dni(dato[4])
            dato2 = dato[5].split(",")
            for item in dato2:
                if item[-1] == '\n':
                    item = item.rstrip("\n")
                    mi_piloto.agregar_modelo_avion(item)
            lista_personas.append(mi_piloto)

        elif (dato [0] == "Servicio"):
            mi_tripulante_servicio = servicio()
            mi_tripulante_servicio.modelos_avion_permitidos = []
            mi_tripulante_servicio.agregar_nombre(dato[1])
            mi_tripulante_servicio.agregar_apellido(dato[2])
            dato2 = dato[3].split("-")
            mi_tripulante_servicio.agregar_fecha_nacimiento(date (int(dato2[2]) ,int(dato2[1]) , int(dato2[0])))
            mi_tripulante_servicio.agregar_dni(dato[4])
            dato2 = dato[5].split(",")
            for item in dato2:
                mi_tripulante_servicio.agregar_modelo_avion(item)
            dato2 = dato[6].split(",")
            for item in dato2:
                if item[-1] == '\n':
                    item = item.rstrip("\n")
                    mi_tripulante_servicio.agregar_idioma(item)
            lista_personas.append(mi_tripulante_servicio)

arc_personas.close()


arc_aviones = open("aviones.dat", "r")
for line in arc_aviones:
    dato = line.split("|")
    mi_avion = aviones()
    mi_avion.agregar_codigo_avion(dato[0])
    mi_avion.agregar_cant_pasajeros(dato[1])
    if dato[-1][-1] == '\n':
        dato[-1] = dato[-1].rstrip("\n")
        mi_avion.agregar_cant_tripulacion(dato[2])
    lista_aviones.append(mi_avion)

arc_personas.close()

arc_vuelos = open("vuelos.dat", "r")
for line in arc_vuelos:
    dato = line.split("|")
    mi_vuelo = vuelos()
    for item in lista_aviones:
        if item.codigo_avion == dato[0]:
            mi_vuelo.agregar_avion(item)
            break
    dato2 = dato[1].split("-")
    mi_vuelo.agregar_fecha(date (int(dato2[2]) ,int(dato2[1]) , int(dato2[0])))
    mi_vuelo.agregar_hora(dato[2])
    mi_vuelo.agregar_origen(dato[3])
    mi_vuelo.agregar_destino(dato[4])

    dato2 = dato[5].split(",")
    for item in dato2:
        for item2 in lista_personas:
            if item2.dni == item:
                mi_vuelo.agregar_tripulacion(item2)
                break

    dato2 = dato[6].split(",")
    for item in dato2:
        if item[-1] == '\n':
            item = item.rstrip("\n")
        for item2 in lista_personas:
            if item2.dni == item:
                mi_vuelo.agregar_pasajero(item2)
    mi_vuelo.agregar_origen(dato[3])
    lista_vuelos.append(mi_vuelo)
arc_vuelos.close()


print ("VUELOS: ")
for item in lista_vuelos:
    print ("NOMINA DE: " + str(item.mostrar_nomina()))
    lista_datos = ["NOMBRE", "APELLIDO", "FECHA NACIMIENTO", "DNI"]
    print("{: >20} {: >20}  {: >20} {: >20}".format(*lista_datos))
    for item2 in item.pasajeros:
        lista_datos = [item2.nombre , item2.apellido , str(item2.fecha_nacimiento) , item2.dni]
        print ("{: >20} {: >20}  {: >20} {: >20}".format(*lista_datos))
    for item2 in item.tripulacion:
        lista_datos = [item2.nombre , item2.apellido , str(item2.fecha_nacimiento) , item2.dni]
        print ("{: >20} {: >20}  {: >20} {: >20}".format(*lista_datos))

print ("\nPASAJERO MAS JOVEN POR VUELO:")
for item in lista_vuelos:
    pasajero = item.mostrar_pasajero_mas_joven ()
    print("\nPASAJERO MAS JOVEN:")
    lista_datos = ["DNI" , "NOMBRE COMPLETO" , "EDAD"]
    print("{: >20} {: >20} {: >20}".format(*lista_datos))
    lista_datos = [pasajero.dni , pasajero.nombre + " " + pasajero.apellido , (str(date.today() - pasajero.fecha_nacimiento))]
    print ("{: >20} {: >20} {: >20}".format(*lista_datos))

print ("TRIPULACION MINIMA por VUELO:\n")
for item in lista_vuelos:
    #sys.stdout.write ("")
    #sys.stdout.flush
    lista_datos = ["VUELO" , "ORIGEN" , "DESTINO" , "ESTADO" , "MINIMA - TOTAL"]
    print("{: >20} {: >20} {: >20} {: >20} {: >15}".format(*lista_datos))
    lista_datos = ["no hay iden." , item.origen , item.destino , str(item.tripulacion_minima()) , str(item.avion.cant_tripulacion) +
                   " - " + str(len(item.tripulacion))]
    print ("{: >20} {: >20} {: >20} {: >20} {: >15}".format(*lista_datos))

print ("\nTRIPULACION INCORRECTA:")
for item in lista_vuelos:
    print ("VUELO:")
    lista_datos = item.comprobar_tripulacion()
    if len(lista_datos) == 0:
        print ("TODO ESTA CORRECTO\n")
    else:
        print ("HAY ERRORES: ")
        lista_datos2 = ["TRIPULANTE" , "DNI" , "AVIONES PERMITIDOS" , "MODELO DE AVION DEL VUELO"]
        print("{: >20} {: >20} {: >30} {: >30}".format(*lista_datos2))
        for item2 in lista_datos:
            lista_datos2 = [item2.nombre + " " + item2.apellido, item2.dni, item2.modelos_avion_permitidos[0], #no muestra modelos de avion del item2
                            item.avion.codigo_avion]
            print("{: >20} {: >20} {: >30} {: >30}".format(*lista_datos2))

print ("\nTRIPULANTES QUE VUELAN MULTIPLES VECES POR DIA:")
lista_repetidos = []
for item in lista_vuelos:
    for item3 in lista_vuelos:
        if (item == item3) or (item.fecha != item3.fecha):
            continue
        for item2 in item.tripulacion:
            for item4 in item3.tripulacion:
                if (item2 == item4):
                    if len(lista_repetidos) == 0:
                        lista_repetidos.append([item4 , item , item3])
                    else:
                        existe = False
                        for item5 in lista_repetidos:
                            if ((item5[0] == item4) and ((item5[1] == item) and (item5[2] == item3)) or ((item5[2] == item) and (item5[1] == item3))):
                                existe = True
                                break
                        if existe == False:
                            lista_repetidos.append([item4, item, item3])

if len(lista_repetidos) == 0:
    print ("NO HAY ERROR. NO HAY ERROR. LA MONARQUIA ESPANIOLA")
else:
    lista_datos = ["DNI", "NOMBRE COMPLETO", "AVION 1", "AVION 2" , "FECHA"]
    print("{: >20} {: >20} {: >30} {: >30} {: >30}".format(*lista_datos))
    for item in lista_repetidos:
        lista_datos = [item[0].dni , item[0].nombre + " " + item[0].apellido , item[1].origen + " A " + item[1].destino ,
                       item[2].origen + " A " + item[2].destino , str(item[2].fecha)]
        print("{: >20} {: >20} {: >30} {: >30} {: >30}".format(*lista_datos))


print ("\nPASAJEROS CON NECESIDADES ESPECIALES \ vip:")
for item in lista_vuelos:
    print ("\nVUELO:")
    lista_datos = item.personas_con_necesidades_especiales()
    lista_datos2 = ["DNI", "NOMBRE COMPLETO", "VIP", "NECESIDADES ESPECIALES"]
    print("{: >20} {: >20} {: >20} {: >30}".format(*lista_datos2))
    for item in lista_datos:
        lista_datos2 = [item.dni, item.nombre + " " + item.apellido , str(item.dar_vip()) , str(item.dar_necesidades_especiales())]
        print("{: >20} {: >20} {: >20} {: >30}".format(*lista_datos2))