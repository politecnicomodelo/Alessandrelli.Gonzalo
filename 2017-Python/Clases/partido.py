from .equipo import equipo

class partido (object):

    equipos = []
    fechas_partidos = []

    def añadir_equipo (self , equipo):

        self.equipos.append (equipo)

    def ordenar_fechas_partidos (self):

        dia = 0
        dia_actual = dia
        semana = 0
        semana_actual = semana
        partido_creado = None
        terminado = False
        nro_equipos = len(self.equipos)
        equipos_ingresados = 0


        for item in self.equipos:
            partido_creado = None
            semana_actual += 1
            partido_creado += "Semana " + str(semana_actual) + " | "

            while (dia <= 7):
                dia += 1
                if (equipos_ingresados == nro_equipos):
                    break

                elif (dia == 1):
                    partido_creado += "lunes " + " | "
                    for item in self.equipos:
                        if (item [1] == "1"):


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