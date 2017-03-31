from .jugador import jugador

class equipo (object):

    Nombre = ""
    localidad = ""
    lista_jugadores = []
    capitan = None
    turnos = []

    def agregar_nombre (self , nombre):

        self.nombre = str(nombre)

    def agregar_localidad (self , localidad):

        self.localidad = str(localidad)

    def agregar_jugadores (self , jugador):

        for item in self.lista_jugadores:
            if (item.numero_camisa == jugador.numero_camisa):
                return False
            else:
                self.lista_jugadores.append (jugador)

    def agregar_capitan (self , numero_camisa):

        for item in self.lista_jugadores:
            if (item.numero_camisa == numero_camisa):
                self.capitan = item
                return True
        return False


    def agregar_turnos (self , turno , dia):

        if ((str(turno) != "manana") and (str(turno) != "tarde") and (str(turno) != "noche")):
            return False
        elif ((str(dia) != "lunes") and (str(dia) != "martes") and (str(dia) != "miercoles") and (str(dia) != "jueves") and (str(dia) != "viernes") and (str(dia) != "sabado")):
             return False
        else:

            if (turno == "manana"):
                turno = "a"

            elif (turno == "tarde"):
                turno = "b"

            elif (turno == "noche"):
                turno = "c"

            if (dia == "lunes"):
                dia = "1"
            elif (dia == "martes"):
                dia = "2"
            elif (dia == "miercoles"):
                dia = "3"
            elif (dia == "jueves"):
                dia = "4"
            elif (dia == "viernes"):
                dia = "5"
            elif (dia == "sabado"):
                dia = "6"

            self.turnos.append (urno + dia)