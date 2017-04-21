from .vehiculo import vehiculo

class camioneta (vehiculo):
    capacidad_carga = None

    def set_capacidad_carga (self , capacidad_carga):
        self.capacidad_carga = capacidad_carga
