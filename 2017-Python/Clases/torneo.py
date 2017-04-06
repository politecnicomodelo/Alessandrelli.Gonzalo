from .equipo import equipo
from .partido import partido


class torneo (object):
    equipos = []
    partidos_creados = []
    equipos_emparejados = []

    def añadir_equipo(self, equipo):

        self.equipos.append(equipo)

    def ordenar_fechas_partidos(self):

        dia = 0
        semana = 0
        partido_creado = None
        abortar = False
        terminado = False
        turno = "a"

        a = 1
        partidos_a_crear = 0
        while (a > len(self.equipos)):
            partidos_a_crear += len(self.equipos) - 1
        partidos_establecidos = 0

        partido_creado = None
        semana_actual += 1

        while (True):
            if (dia == 7):
                dia = 0
                semana += 1
            dia += 1
            turno = "a"

            while (turno != "d"):
                for item in self.equipos:
                    for item_2 in self.equipos[item].turnos:
                        if ((item_2[1] == str(dia)) and (item_2[0] == turno)):
                            for item_3 in self.equipos:
                                if (item_3 != item):
                                    posicion = 0
                                    for item_5 in self.equipos_emparejados:
                                        if (((item_5[posicion][0] == item) and (item_5[posicion][1] == item_3)) or (
                                            (item_5[posicion][0] == item_3) and (item_5[posicion][1] == item))):
                                            abortar = True
                                            break
                                        posicion += 1
                                    for item_4 in self.equipos[item_3].turnos:
                                        if (abortar == True):
                                            abortar = False
                                            break
                                        if ((item_4[1] == str(dia)) and (item_4[0] == turno)):
                                            nuevo_partido = partido (item , item_3 , semana , dia , turno)
                                            self.partidos_creados.append (nuevo_partido)
                                            #self.equipos_emparejados.append([item, item_3])
                                            partidos_establecidos += 1
                                            if (partidos_establecidos == partidos_a_crear):
                                                terminado = True
                                            break
                            if ((turno_usado == True) or (terminado == True)):
                                break

                    if ((turno_usado == True) or (terminado == True)):
                        turno_usado = False
                        break

                if (turno == "a"):
                    turno = "b"
                elif (turno == "b"):
                    turno = "c"
                elif (turno == "c"):
                    turno = "d"

            if (terminado == True):
                break