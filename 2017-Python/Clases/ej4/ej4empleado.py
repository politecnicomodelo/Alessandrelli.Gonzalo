from datetime import date

class empleado (object):

    Nombre = ""
    Apellido = ""
    telefono = None
    FechaDeNacimiento = None
    dias_laborales = []
    asistencias = []
    identificador = None


    def set_nombre (self , nombre):
        self.nombre = nombre

    def set_apellido (self , apellido):
        self.apellido = apellido

    def set_fecha_nacimiento (self , a , m , d):
        self.FechaDeNacimiento = date (a,m,d)

    def set_telefono (self , telefono):
        self.telefono = telefono

    def dias_de_labor (self , dia):
        self.dias_laborales.append (dia)

    def asistencia (self , datos):
        self.asistencias.append (datos)

    def por_asistencias_mes (self , mes):
        asistencias = 0
        for item in self.asistencias:
            if item [2] == mes:
                asistencias += 1

        return (asistencias * 100) / (len(self.dias_laborales) * 4)

    def set_idenficador (self , identificador):
        self.identificador = identificador

