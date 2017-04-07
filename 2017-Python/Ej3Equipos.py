from Clases.equipo import equipo
from Clases.jugador import jugador
from Clases.partido import partido
from Clases.torneo import torneo
from datetime import date

torneo = torneo ()

equipo_1 = equipo ()
equipo_2 = equipo ()

jugador_1 = jugador ()
jugador_2 = jugador ()
jugador_3 = jugador ()
jugador_4 = jugador ()
jugador_5 = jugador ()
jugador_6 = jugador ()
jugador_7 = jugador ()
jugador_8 = jugador ()
jugador_9 = jugador ()
jugador_10 = jugador ()

dia = None
Mes = None
ano = None

equipo_1.agregar_nombre (input ("ingrese un nombre para el equipo 1: "))
equipo_1.agregar_localidad (input ("ingrese una localidad para el equipo 1: "))

jugador_1.agregar_nombre(input ("ingrese un nombre para el jugador 1: "))
jugador_1.agregar_numero_camisa (input ("ingrese un numero de camisa para el jugador 1: "))
dia = input ("Ingrese el dia de nacimiento para el jugador 1 (solo dia, y numericamente): ")
mes = input ("Ingrese el mes de nacimiento para el jugador 1 (solo mes, y numericamente): ")
ano = input ("Ingrese el ano de nacimiento para el jugador 1 (solo ano, y numericamente): ")
jugador_1.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
equipo_1.agregar_jugadores (jugador_1)

while (True):
    jugador_2.agregar_nombre (input ("ingrese un nombre para el jugador 2: "))
    jugador_2.agregar_numero_camisa (input("ingrese un numero de camisa para el jugador 2: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 2 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 2 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 2 (solo ano, y numericamente): ")
    jugador_2.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_1.agregar_jugadores (jugador_2) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    if equipo_1.agregar_capitan (input ("ingrese el numero de camisa del capitan: ")) == False:
        print ("No existe ese numero de camisa en el equipo, reingrese el dato: ")
        print (equipo_1.lista_jugadores)
    else:
        break

posicion = 1
turno = None
dia = None
while posicion <= 18:
    turno = input ("agregar turno (MANANA/TARDE/NOCHE/) (s para salir): ")
    if turno == "s":
        break
    elif (turno == "manana"):
        turno = 0
    elif (turno == "tarde"):
        turno = 1
    elif (turno == "noche"):
        turno = 2
    dia = input("agregar turno (LUNES/MARTES/MIERCOLES/JUEVES/VIERNES/SABADO): ")
    if (dia == "lunes"):
        dia = 0
    elif (dia == "martes"):
        dia = 1
    elif (dia == "miercoles"):
        dia = 2
    elif (dia == "jueves"):
        dia = 3
    elif (dia == "viernes"):
        dia = 4
    elif (dia == "sabado"):
        dia = 5
    elif (dia == "domingo"):
        dia = 6

    equipo_1.agregar_turnos (turno , dia)
    posicion += 1
    if (posicion == 18):
        print ("se excedio el maximo numero de turnos")
        break

equipo_2.agregar_nombre(input("ingrese un nombre: "))
equipo_2.agregar_localidad(input("ingrese una localidad: "))

jugador_6.agregar_nombre (input ("ingrese un nombre: "))
jugador_6.agregar_numero_camisa (input("ingrese un numero de camisa: "))
dia = input ("Ingrese el dia de nacimiento para el jugador 6 (solo dia, y numericamente): ")
mes = input ("Ingrese el mes de nacimiento para el jugador 6 (solo mes, y numericamente): ")
ano = input ("Ingrese el ano de nacimiento para el jugador 6 (solo ano, y numericamente): ")
jugador_6.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
equipo_2.agregar_jugadores(jugador_6)

while (True):
    jugador_7.agregar_nombre (input ("ingrese un nombre: "))
    jugador_7.agregar_numero_camisa (input("ingrese un numero de camisa: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 6 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 6 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 6 (solo ano, y numericamente): ")
    jugador_6.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_2.agregar_jugadores(jugador_7) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

    while (True):
        if equipo_2.agregar_capitan(input("ingrese el numero de camisa del capitan: ")) == False:
            print ("No existe ese numero de camisa en el equipo, reingrese el dato: ")
            print (equipo_2.lista_jugadores)
        else:
            break

posicion = 1
turno = None
dia = None
while posicion <= 18:
    turno = input("agregar turno (MANANA/TARDE/NOCHE/) (s para salir): ")
    if turno == "s":
        break
    elif (turno == "manana"):
        turno = 0
    elif (turno == "tarde"):
        turno = 1
    elif (turno == "noche"):
        turno = 2
    dia = input("agregar turno (LUNES/MARTES/MIERCOLES/JUEVES/VIERNES/SABADO): ")
    if (dia == "lunes"):
        dia = 0
    elif (dia == "martes"):
        dia = 1
    elif (dia == "miercoles"):
        dia = 2
    elif (dia == "jueves"):
        dia = 3
    elif (dia == "viernes"):
        dia = 4
    elif (dia == "sabado"):
        dia = 5
    elif (dia == "domingo"):
        dia = 6
    equipo_2.agregar_turnos(turno, dia)
    posicion += 1
    if (posicion == 18):
        print ("se excedio el maximo numero de turnos")
        break

print (equipo_1.turnos)
print (equipo_2.turnos)

torneo.añadir_equipo (equipo_1)
torneo.añadir_equipo (equipo_2)


for item in torneo.equipos:
    print (item.nombre)

if (torneo.ordenar_fechas_partidos () == False):
    print ("Se produjo un error al crear los aprtidos...lol")
else:
    print ("partidos creados exitosamente:")

    for item in torneo.partidos_creados:
        print (item.equipo_1.nombre , " vs ")
        print (item.equipo_2.nombre , " | semana: " , item.semana , " | dia: ")
        print (item.dia + 1 , " turno: ")
        print (item.turno + 1)