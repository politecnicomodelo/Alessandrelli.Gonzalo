from datetime import date

class aviones (object):
    codigo_avion = None
    cant_pasajeros = None
    cant_tripulacion = None

    def agregar_codigo_avion (self , codigo_avion):
        self.codigo_avion = str(codigo_avion)

    def agregar_cant_pasajeros (self , cant):
        self.cant_pasajeros = str(cant)

    def agregar_cant_tripulacion (self , cant):
        self.cant_tripulacion = str(cant)