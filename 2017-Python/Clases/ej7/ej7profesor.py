from .ej7persona import persona


class profesor(persona):

    def dar_desc (self):
        return self.descuento

    def agregar_desc (self , descuento):
        self.descuento = descuento