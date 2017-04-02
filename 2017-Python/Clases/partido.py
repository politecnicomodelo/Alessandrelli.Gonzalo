from .equipo import equipo

class partido (object):

    equipos = []
    fechas_partidos = []
    equipos_emparejados = []

    def añadir_equipo (self , equipo):

        self.equipos.append (equipo)

    def ordenar_fechas_partidos (self):

        dia = 0
        semana = 0
        semana_actual = semana
        partido_creado = None
        terminado = False
        turno = "a"
        abortar = False
        pareja_de_equipos = []
        turno_usado = False

        a = 1
        partidos_a_crear = 0
        while (a > len (self.equipos)):
            partidos_a_crear += len (self.equipos) - 1

        partidos_establecidos = 0

        for item in self.equipos:
            partido_creado = None
            semana_actual += 1

            while (True):
                if (dia == 7):
                    dia = 0
                    semana_actual += 1;
                dia += 1
                turno = "a"

                if (dia == 1):

                    while (turno != "d"):
                        for item in self.equipos:
                            for item_2 in self.equipos [item].turnos:
                                if (item_2 [1] == str (dia)):
                                    if (item_2 [0] == turno):
                                        for item_3 in self.equipos:
                                            if (item_3 != item):
                                                posicion = 0
                                                for item_5 in self.equipos_emparejados:
                                                    if (((item_5 [posicion] [0] == item) and (item_5 [posicion] [1] == item_3)) or ((item_5 [posicion] [0] == item_3) and (item_5 [posicion] [1] == item))):
                                                        abortar = True
                                                        break
                                                    posicion += 1
                                                for item_4 in self.equipos [item_3].turnos:
                                                    if (abortar == True):
                                                        abortar = False
                                                        break
                                                    if (item_4[1] == str(dia)):
                                                        if (item_4[0] == turno):
                                                            partido_creado += "Semana " + str(semana_actual) + " | " + "lunes " + " | " + item.nombre + " vs " + item_3.nombre
                                                            pareja_de_equipos.append (item , item_3)
                                                            self.equipos_emparejados.append (pareja_de_equipos)
                                                            pareja_de_equipos = []
                                                            self.fechas_partidos.append (partido_creado)
                                                            partido_creado = None
                                                            turno_usado = True
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
                        elif(turno == "c"):
                            turno = "d"

                        if (terminado == True):
                            break


                elif (dia == 2):
                    partido_creado += "martes " + " | "



                elif (dia == 3):
                    partido_creado += "miercoles " + " | "



                elif (dia == 4):
                    partido_creado += "jueves " + " | "



                elif (dia == 5):
                    partido_creado += "vienes " + " | "



                elif (dia == 6):
                    partido_creado += "sabado " + " | "



                elif (dia == 7):
                    partido_creado += "domingo " + " | NO SE JUEGA"
                    break