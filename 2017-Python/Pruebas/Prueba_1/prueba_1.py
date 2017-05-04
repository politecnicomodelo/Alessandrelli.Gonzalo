from Clases.prueba_1_persona import persona
from Clases.prueba_1_peso_altura_fecha import relacion
from datetime import date

mi_persona = persona ()
mis_datos = relacion ()

mi_persona.set_nombre ("juan")
mi_persona.set_apellido ("manuel")
mi_persona.set_fecha_nacimiento (date (1999 , 8 , 18))

mis_datos.set_datos (80 , 60 , date (2000 , 2 , 1))
mi_persona.agregar_datos (mis_datos)

mis_datos.set_datos (100 , 50 , date (2000 , 1 , 1))
mi_persona.agregar_datos (mis_datos)

mis_datos.set_datos (100 , 100 , date (2001 , 1 , 1))
mi_persona.agregar_datos (mis_datos)

print (( 1.7 * 100) / 1)

print ("promedio peso: " , mi_persona.promedio_peso (2000))

print ("promedio altura: " , mi_persona.promedio_peso (2000))

print ("porcentaje altura: " , mi_persona.promedio_peso (2000 , 2001))



#QUERIDO PROFE
#SI NO SE PUEDEN HACER BIEN LAS CONSULTAS ES PORQUE SE REPITEN LOS DATOS, Y NO LO PUEDO ARREGLAR AUNQUE PONGA UN __INIT__