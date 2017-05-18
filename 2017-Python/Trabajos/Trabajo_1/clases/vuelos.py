from datetime import date

class vuelos (object):
    avion = None
    fecha = None
    hora = None
    origen = None
    destino = None
    tripulacion = []
    pasajeros = []

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
