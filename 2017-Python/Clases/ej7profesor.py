from .persona import persona


class profesor(persona):
    descuento = None

    def dar_desc (self):
        return self.descuento

    def agregar_desc (self , descuento):
        self.descuento = descuento