
class persona (object):
    nombre = None
    apellido = None
    descuento = None
    dni = None

    def dar_desc (self):
        return 0

    def agregar_nombre (self, nombre):
        self.nombre = nombre

    def agregar_apellido (self, apellido):
        self.apellido = apellido

    def agregar_dni (self, dni):
        self.dni = dni