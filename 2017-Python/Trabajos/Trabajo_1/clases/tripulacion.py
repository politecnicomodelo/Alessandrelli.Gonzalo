from datetime import date
from .personas import persona

class tripulacion (persona):
    modelos_avion_permitidos = []

    def agregar_modelo_avion (self , modelo):
        self.modelos_avion_permitidos.append (str(modelo))
