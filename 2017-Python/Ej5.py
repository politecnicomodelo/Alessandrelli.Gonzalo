from Clases.empresa_automovilistica import empresa
from Clases.camioneta import camioneta
from Clases.auto import auto

mi_empresa = empresa ()
mi_auto = auto ()
mi_camioneta = camioneta ()

mi_auto.set_patente ("gay 123")
mi_auto.set_cant_ruedas (5)
mi_auto.set_anio_fabricacion (1970)
mi_auto.set_descapotable (True)

mi_empresa.agregar_auto (mi_auto)

mi_camioneta.set_patente ("gay 124")
mi_camioneta.set_cant_ruedas (7)
mi_camioneta.set_anio_fabricacion (1971)
mi_camioneta.set_capacidad_carga (2)

mi_empresa.agregar_camioneta (mi_camioneta)