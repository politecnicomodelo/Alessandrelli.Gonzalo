from .equipo import equipo

class partido (object):

    equipo_1 = None
    equipo_2 = None
    semana = None
    dia = None
    turno = None

    def __init__ (self , equipo_1 , equipo_2 , semana , dia , turno):
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.semana = semana
        self.dia = dia
        self.turno = turno