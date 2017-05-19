from datetime import date
from clases.tripulacion import tripulacion
from clases.piloto import piloto
from clases.servicio import servicio
from clases.pasajero import pasajero
from clases.aviones import aviones
from clases.vuelos import vuelos

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
            mi_pasajero.agregar_vip(dato[5])
            mi_pasajero.agregar_necesidades_especiales(dato[6])
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
                mi_piloto.agregar_modelo_avion(item)
            lista_personas.append(mi_piloto)

        elif (dato [0] == "Servicio"):
            mi_tripulante_servicio = servicio()
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
                mi_tripulante_servicio.agregar_idioma(item)
            lista_personas.append(mi_tripulante_servicio)

arc_personas.close()


arc_aviones = open("aviones.dat", "r")
for line in arc_aviones:
    dato = line.split("|")
    mi_avion = aviones()
    mi_avion.agregar_codigo_avion(dato[0])
    mi_avion.agregar_cant_pasajeros(dato[1])
    mi_avion.agregar_cant_tripulacion(dato[2])
    lista_aviones.append(mi_avion)

arc_personas.close()

arc_vuelos = open("vuelos.dat", "r")
for line in arc_vuelos:
    dato = line.split("|")
    mi_vuelo = vuelos()
    mi_vuelo.agregar_avion(dato[0])
    dato2 = dato[1].split("-")
    mi_vuelo.agregar_fecha(date (int(dato2[2]) ,int(dato2[1]) , int(dato2[0])))
    mi_vuelo.agregar_hora(dato[2])
    mi_vuelo.agregar_origen(dato[3])
    mi_vuelo.agregar_destino(dato[4])
    dato2 = dato[5].split(",")
    for item in dato2:
        mi_vuelo.agregar_tripulacion(item)
    dato2 = dato[6].split(",")
    for item in dato2:
        mi_vuelo.agregar_pasajero(item)
    mi_vuelo.agregar_origen(dato[3])
    lista_vuelos.append(mi_vuelo)

arc_vuelos.close()

