from datetime import date
from .tripulacion import tripulacion

class servicio (tripulacion):
    idiomas = []

    def __init__(self):
        self.idiomas = []

    def agregar_idioma (self , idioma):
        self.idiomas.append (idioma)