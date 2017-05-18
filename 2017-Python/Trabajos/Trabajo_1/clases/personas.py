from datetime import date

class persona (object):
    dni = None
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def agregar_dni (self , dni):
        self.dni = str(dni)

    def agregar_nombre (self , nombre):
        self.nombre = str(nombre)

    def agregar_apellido (self , apellido):
        self.apellido = str(apellido)

    def agregar_fecha_nacimiento (self , fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento


    def dar_vip (self):
        return False

    def dar_necesidades_especiales (self):
        return False