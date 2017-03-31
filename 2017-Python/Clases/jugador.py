from datetime import date

class jugador (object):

    Nombre = ""
    numero_camisa = None
    fecha_nacimiento = None

    def agregar_nombre (self , nombre):

        self.nombre = str(nombre)

    def agregar_numero_camisa (self, numero_camisa):

        self.numero_camisa = numero_camisa

    def agregar_fecha_nacimiento (self, fecha_nacimiento):

        self.fecha_nacimiento = fecha_nacimiento