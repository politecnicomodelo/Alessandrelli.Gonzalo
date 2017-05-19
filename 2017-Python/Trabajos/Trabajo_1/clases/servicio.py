from datetime import date
from .tripulacion import tripulacion

class servicio (tripulacion):
    idiomas = []

    def agregar_idioma (self , idioma):
        self.idiomas.append (idioma)