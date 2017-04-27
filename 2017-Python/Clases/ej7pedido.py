from datetime import date
from .alumno import alumno
from .profesor import profesor

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
        self.plato.precio = self.plato.precio - ((self.plato.precio / 100) * persona.dar_desc ())

    def agregar_hora_entrega (self , hora_entrega):
        self.hora_entrega = hora_entrega

    def establecer_estado (self, estado):
        self.estado = estado

    def establecer_nro_pedido (self , nro_pedido):
        self.nro_pedido = nro_pedido