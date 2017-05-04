from .ej4empleado import empleado

class empresa (object):

    Nombre = ""
    telefono = None
    empleados = []

    def set_nombre (self , nombre):
        self.nombre = nombre

    def set_telefono (self , telefono):
        self.telefono = telefono

    def agregar_empleado (self , empleado):
        self.empleados.append (empleado)

    def calcular_porcentaje_asistencias (self , identificador , mes):
        for item in empleados:
            if item.identificador == identificador:
                item.por_asistencias_mes (mes)
