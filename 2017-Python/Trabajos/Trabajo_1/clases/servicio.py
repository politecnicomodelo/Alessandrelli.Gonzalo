from datetime import date
from .tripulacion import tripulacion

class servicio (tripulacion):
    idiomas = None

    def agregar_idioma (self , idioma):
        self.idiomas.append (idioma)