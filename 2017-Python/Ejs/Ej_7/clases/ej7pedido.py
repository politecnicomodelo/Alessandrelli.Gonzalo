from datetime import date
from .ej7alumno import alumno
from .ej7plato import plato
from .ej7profesor import profesor


class pedido (object):
    fecha_creacion = None
    plato = None
    persona = None
    hora_entrega = None
    estado = None
    nro_pedido = None

    def agregar_fecha_creacion (self , fecha_creacion):
        self.fecha_creacion = fecha_creacion

    def agregar_plato (self , plato):
        self.plato = plato

    def agregar_persona (self , persona):
        self.persona = persona

    def agregar_hora_entrega (self , hora_entrega):
        self.hora_entrega = hora_entrega

    def establecer_estado (self, estado):
        self.estado = estado

    def establecer_nro_pedido (self , nro_pedido):
        self.nro_pedido = nro_pedido

    def __str__(self):
        return str ("\nNRO. PEDIDO: " + str (self.nro_pedido) + "\nCREACION: " + str (self.fecha_creacion) + "\nPERSONA: "
                   + str (self.persona.dni) + "\nDESCUENTO DE LA PERSONA: " + str (self.persona.dar_desc ()) + "\nNOMBRE PLATO: "
                   + str (self.plato.nombre) + "\nPRECIO PLATO: " + str (self.plato.precio) + "\nPRECIO PLATO CON DESCUENTO: "
                   + str (self.dar_precio_con_desc()) + "\nHORA ENTREGA: "
                   + str (self.hora_entrega + "\nESTADO PEDIDO: " + self.estado))

    def dar_precio_con_desc (self):
        return (int (self.plato.precio) - ((int (self.plato.precio) / 100) * int (self.persona.dar_desc ())))