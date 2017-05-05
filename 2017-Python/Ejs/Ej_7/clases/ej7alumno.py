from .ej7persona import persona

class alumno (persona):
    division = None

    def agregar_division (self , division):
        self.division = division