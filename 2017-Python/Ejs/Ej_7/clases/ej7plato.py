
class plato (object):
    nombre = None
    precio = None

    def agregar_nombre(self , nombre):
        self.nombre = nombre

    def agregar_precio(self , precio):
        self.precio = precio

    def __str__(self):
        return str ("nombre: " + str(self.nombre) + " | precio: " + str(self.precio) + "\n")
