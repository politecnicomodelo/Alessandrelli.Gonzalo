class materia (object):

    Nombre = ""
    ListaDeNotas = []

    def __init__(self):
        self.ListaDeNotas = []

    def SetNombre (self , n):
        self.nombre = n

    def AgregarNota (self , n):
        self.ListaDeNotas.append (n)

