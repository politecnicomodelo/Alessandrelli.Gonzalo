from .jugador import jugador

class equipo (object):

    nombre = ""
    localidad = ""
    lista_jugadores = []
    capitan = None
    turnos = []

    def __init__(self):
        self.lista_jugadores = []
        self.turnos = []

    def agregar_nombre (self , nombre):

        self.nombre = str(nombre)

    def agregar_localidad (self , localidad):

        self.localidad = str(localidad)

    def agregar_jugadores (self , jugador):

        for item in self.lista_jugadores:
            if (item.numero_camisa == jugador.numero_camisa):
                return False
        self.lista_jugadores.append (jugador)
        return True

    def agregar_capitan (self , numero_camisa):

        for item in self.lista_jugadores:
            if (item.numero_camisa == numero_camisa):
                self.capitan = item
                return True
        return False


    def agregar_turnos (self , turno , dia):

        if ((turno != 0) and (turno != 1) and (turno != 2)):
            return False
        elif ((dia != 0) and (dia != 1) and (dia != 2) and (dia != 3) and (dia != 4) and (dia != 5) and (dia != 6)):
             return False
        else:
            self.turnos.append ([turno , dia])