from .Lugar import lugar

class barrio (lugar):
    poblacion = None
    ciudad_perteneciente = None

    def soy(cls):
        return "barrio"