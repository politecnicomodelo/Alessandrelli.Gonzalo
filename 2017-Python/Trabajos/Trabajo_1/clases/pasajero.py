from datetime import date
from .personas import persona

class pasajero (persona):
    vip = False
    necesidades_especiales = False

    def agregar_vip (self , vip):
        self.vip = vip

    def agregar_necesidades_especiales (self , necesidad):
        self.necesidades_especiales = necesidad

    def agregar_millas_viajadas (self , millas):
        self.millas_viajadas = millas

    def dar_vip (self):
        return self.vip

    def dar_necesidades_especiales (self):
        return self.necesidades_especiales