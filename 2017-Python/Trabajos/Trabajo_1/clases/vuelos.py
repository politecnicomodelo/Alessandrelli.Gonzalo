from datetime import date
from datetime import datetime

class vuelos (object):
    avion = None
    fecha = None
    hora = None
    origen = None
    destino = None
    tripulacion = []
    pasajeros = []

    def __init__(self):
        self.tripulacion = []
        self.pasajeros = []

    def agregar_avion (self , avion):
        self.avion = avion

    def agregar_fecha (self , fecha):
        self.fecha = fecha

    def agregar_hora (self , hora):
        self.hora = hora

    def agregar_origen (self , origen):
        self.origen = origen

    def agregar_destino (self , destino):
        self.destino = destino

    def agregar_tripulacion (self , tripulante):
        self.tripulacion.append (tripulante)

    def agregar_pasajero (self , pasajero):
        self.pasajeros.append (pasajero)

    def mostrar_nomina (self):
        return (len(self.pasajeros) + len(self.tripulacion))

    def mostrar_pasajero_mas_joven (self):
        pasajero = None

        for item in self.pasajeros:
            if pasajero == None:
                pasajero = item
            elif datetime.today().date() - item.fecha_nacimiento < datetime.today().date() - pasajero.fecha_nacimiento:
                pasajero = item
        return pasajero

    def tripulacion_minima (self):
        if int(self.avion.cant_tripulacion) > len(self.tripulacion):
            return False
        return True

    def comprobar_tripulacion (self):
        lista_tripulacion_incorrecta = []
        for item in self.tripulacion:
            for item2 in item.modelos_avion_permitidos:
                if ((item2 != self.avion.codigo_avion) and (item == item.modelos_avion_permitidos [-1])):
                    lista_tripulacion_incorrecta.append(item)
        return lista_tripulacion_incorrecta

    def personas_con_necesidades_especiales (self):
            lista_personas = []
            for item in self.tripulacion:
                if item.dar_vip() != False or item.dar_necesidades_especiales != False:
                    lista_personas.append(item)
            return lista_personas