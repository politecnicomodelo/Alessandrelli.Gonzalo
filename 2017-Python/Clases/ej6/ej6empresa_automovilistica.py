from .ej6vehiculo import vehiculo

class empresa (object):
    lista_camionetas = []
    lista_autos = []

    def __init__ (self):
        self.lista_camionetas = []
        self.lista_autos = []

    def agregar_camioneta (self , camioneta):
        self.lista_camionetas.append (camioneta)

    def agregar_auto (self , auto):
        self.lista_autos.append (auto)