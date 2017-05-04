from datetime import date
from. prueba_1_peso_altura_fecha import relacion

class persona (object):
    nombre = None
    apellido = None
    Fecha_nacimiento = None
    datos_peso_altura_fecha = None

    def __init__(self):
        self.datos_peso_altura_fecha = []

    def set_nombre (self , nombre):
        self.nombre = str (nombre)
        return true

    def set_apellido (self , apellido):
        self.apellido = str (apellido)
        return True

    def set_fecha_nacimiento (self , fecha):
        self.Fecha_nacimiento = fecha
        return True

    def agregar_datos (self , datos):
        self.datos_peso_altura_fecha.append (datos)
        return True

    def promedio_peso(self, anio):
        peso_total = 0
        recopilaciones = 0
        for item in self.datos_peso_altura_fecha:
            if ((item.fecha >= date(anio, 1, 1)) and (item.fecha < date(anio + 1, 1, 1))):
                recopilaciones += 1
                peso_total += item.peso

        if (recopilaciones == 0):
            return False

        return peso_total / recopilaciones

    def promedio_altura(self, anio):
        altura_total = 0
        recopilaciones = 0
        for item in self.datos_peso_altura_fecha:
            if ((item.fecha >= date(anio, 1, 1)) and (item.fecha < date(anio + 1, 1, 1))):
                recopilaciones += 1
                altura_total += item.altura

        if (recopilaciones == 0):
            return False

        return altura_total / recopilaciones

    def porcentaje_altura (self, anio_1 , anio_2):
        altura_1 = None
        altura_2 = None
        fecha_actual = None

        for item in self.datos_peso_altura_fecha:
            if ((item.fecha >= date(anio_1, 1, 1)) and (item.fecha < date(anio_1 + 1, 1, 1))):
                if (fecha_actual == None):
                    altura_1 = item.altura
                elif (fecha_actual >= item.fecha):
                    fecha_actual = item.fecha
                    altura_1 = item.altura

        if (altura_1 == None):
            return False

        fecha_actual = None

        for item in self.datos_peso_altura_fecha:
            if ((item.fecha >= date(anio_2, 1, 1)) and (item.fecha < date(anio_2 + 1, 1, 1))):
                if (fecha_actual == None):
                    altura_2 = item.altura
                elif item.fecha >= fecha_actual:
                    fecha_actual = item.fecha
                    altura_2 = item.altura

        if (altura_2 == None):
            return False

        return (((altura_2 * 100) / altura_1) - 100)