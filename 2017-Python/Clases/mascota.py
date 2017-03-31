class mascota (object):

    nombre = ""
    tipo = ""

    def SetNombre (self , n):
        self.nombre = str (n)

    def SetTipo (self , t):
        self.tipo = str (t)

    def QuienSoy (self):
        return "soy " + self.nombre + " y soy un/a " + self.tipo