from Clases.equipo import equipo
from Clases.jugador import jugador
from Clases.partido import partido
from datetime import date

torneo = partido ()

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
    jugador_3.agregar_nombre (input ("ingrese un nombre para el jugador 3: "))
    jugador_3.agregar_numero_camisa (input("ingrese un numero de camisa para el jugador 3: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 3 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 3 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 3 (solo ano, y numericamente): ")
    jugador_3.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_1.agregar_jugadores(jugador_3) == False:
            print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    jugador_4.agregar_nombre (input ("ingrese un nombre para el jugador 4: "))
    jugador_4.agregar_numero_camisa (input("ingrese un numero de camisa para el jugador 4: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 4 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 4 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 4 (solo ano, y numericamente): ")
    jugador_4.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_1.agregar_jugadores (jugador_4) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    jugador_5.agregar_nombre (input ("ingrese un nombre para el jugador 5: "))
    jugador_5.agregar_numero_camisa (input("ingrese un numero de camisa para el jugador 5: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 5 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 5 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 5 (solo ano, y numericamente): ")
    jugador_5.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_1.agregar_jugadores (jugador_5) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    if equipo_1.agregar_capitan (input ("ingrese el numero de camisa del capitan: ")) == False:
        print ("No existe ese numero de camisa en el equipo, reingrese el dato: ")
    else:
        break

posicion = 1
turno = None
dia = None
while posicion <= 18:
    turno = input ("agregar turno (MANANA/TARDE/NOCHE/) (s para salir): ")
    if turno == "s":
        break
    dia = input("agregar turno (LUNES/MARTES/MIERCOLES/JUEVES/VIERNES/SABADO): ")
    equipo_1.agregar_turnos (turno , dia)
    posicion += 1
    if (posicion == 18):
        print ("se excedio el maximo numero de turnos")
        break

torneo.añadir_equipo (equipo_1)

equipo_2.agregar_nombre(input("ingrese un nombre: "))
equipo_2.agregar_localidad(input("ingrese una localidad: "))

jugador_6.agregar_nombre (input ("ingrese un nombre: "))
jugador_6.agregar_numero_camisa (input("ingrese un numero de camisa: "))
dia = input ("Ingrese el dia de nacimiento para el jugador 6 (solo dia, y numericamente): ")
mes = input ("Ingrese el mes de nacimiento para el jugador 6 (solo mes, y numericamente): ")
ano = input ("Ingrese el ano de nacimiento para el jugador 6 (solo ano, y numericamente): ")
jugador_6.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))

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
    jugador_8.agregar_nombre (input ("ingrese un nombre: "))
    jugador_8.agregar_numero_camisa (input("ingrese un numero de camisa: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 7 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 7 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 7 (solo ano, y numericamente): ")
    jugador_7.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_2.agregar_jugadores (jugador_8) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    jugador_9.agregar_nombre (input ("ingrese un nombre: "))
    jugador_9.agregar_numero_camisa (input("ingrese un numero de camisa: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 8 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 8 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 8 (solo ano, y numericamente): ")
    jugador_8.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_2.agregar_jugadores (jugador_9) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    jugador_10.agregar_nombre (input ("ingrese un nombre: "))
    jugador_10.agregar_numero_camisa (input("ingrese un numero de camisa: "))
    dia = input ("Ingrese el dia de nacimiento para el jugador 9 (solo dia, y numericamente): ")
    mes = input ("Ingrese el mes de nacimiento para el jugador 9 (solo mes, y numericamente): ")
    ano = input ("Ingrese el ano de nacimiento para el jugador 9 (solo ano, y numericamente): ")
    jugador_9.agregar_fecha_nacimiento (date (int (ano) , int (mes) , int (dia)))
    if equipo_2.agregar_jugadores (jugador_10) == False:
        print ("numero de camisa ya ingresada, reingrede datos: ")
    else:
        break

while (True):
    if equipo_2.agregar_capitan(input("ingrese el numero de camisa del capitan: ")) == False:
         print ("No existe ese numero de camisa en el equipo, reingrese el dato: ")
    else:
        break

posicion = 1
turno = None
dia = None
while posicion <= 18:
    turno = input("agregar turno (MANANA/TARDE/NOCHE/) (s para salir): ")
    if turno == "s":
        break
    dia = input("agregar turno (LUNES/MARTES/MIERCOLES/JUEVES/VIERNES/SABADO): ")
    equipo_2.agregar_turnos(turno, dia)
    posicion += 1
    if (posicion == 18):
        print ("se excedio el maximo numero de turnos")
        break

torneo.añadir_equipo(equipo_1)