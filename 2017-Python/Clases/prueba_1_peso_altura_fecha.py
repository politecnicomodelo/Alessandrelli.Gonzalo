from datetime import date

class relacion (object):
    peso = None
    altura = None
    fecha = None

    def set_datos (self , peso , altura , fecha):
        self.peso = peso
        self.altura = altura
        self.fecha = fecha
        return True
