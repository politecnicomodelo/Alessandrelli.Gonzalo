from .equipo import equipo
from .partido import partido


class torneo (object):
    equipos = []
    partidos_creados = []

    def __init__(self):
        self.equipos = []
        self.partidos_creados = []

    def añadir_equipo(self, equipo):

        self.equipos.append(equipo)

    def ordenar_fechas_partidos(self):

        dia = -1
        semana = 0
        abortar = False
        turno = 0
        partidos_a_crear = 0
        partidos_establecidos = 0
        terminado = None

        a = 1
        while (a < len(self.equipos)):
            partidos_a_crear += len(self.equipos) - a
            a += 1

        while (True):
            if (dia == 7):
                dia = -1
                semana += 1
            dia += 1
            turno = 0

            while (turno != 3):
                for item in self.equipos:
                    for item_2 in item.turnos:
                        print (item_2[1] , item_2[0] , dia , turno)
                        if ((item_2[1] == dia) and (item_2[0] == turno)):
                            for item_3 in self.equipos:
                                print (item_3.nombre , item.nombre)
                                if (item_3 != item):
                                    posicion = 0
                                    for item_5 in self.partidos_creados:
                                        if (((item_5[posicion][0] == item) and (item_5[posicion][1] == item_3)) or ((item_5[posicion][0] == item_3) and (item_5[posicion][1] == item))):
                                            abortar = True
                                            break
                                        posicion += 1
                                    for item_4 in item_3.turnos:
                                        if (abortar == True):
                                            abortar = False
                                            break
                                        if ((item_4[1] == dia) and (item_4[0] == turno)):
                                            nuevo_partido = partido (item , item_3 , semana , dia , turno)
                                            self.partidos_creados.append (nuevo_partido)
                                            partidos_establecidos += 1
                                            if (partidos_establecidos == partidos_a_crear):
                                                return True
                                            else:
                                                terminado = True
                                                break
                                    if (terminado == True):
                                        break
                                if (terminado == True):
                                    break
                            if (terminado == True):
                                break
                        if (terminado == True):
                             break
                    if (terminado == True):
                        terminado = False
                        break
                turno += 1
