import pygame as pg
from random import randint
import time

pg.init()
pg.font.init()
Pantalla = pg.display.set_mode((1280, 720))
Reloj = pg.time.Clock()
fps = 60
Terminado = False


numeroLlegar = 23 #Numero para ganar
Total = 0 #Lo que se va sumando
maximoSuma = 4 #Cuanto se puede sumar de maximo
Oponente = False #True: vs Computadora, False: vs Oponente
Empezar = False #True: Empezas, False: Empieza la compu

Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 46) #Fotos, etc
Ganar = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Termino.png") #Fotos, etc
Fondo2 = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Fondo.png") #Fotos, etc
Cuadrado = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Cuadrado.png") #Fotos, etc
Computadora = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Computadora.png") #Fotos, etc
OponenteF = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Oponente.png") #Fotos, etc
EmpiezaC = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/EmpiezaCompu.png") #Fotos, etc
EmpiezoY = pg.image.load("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/EmpiezoYo.png") #Fotos, etc
Numero2 = Fuente.render(str(maximoSuma), 1, pg.Color("white")) #Fotos, etc
Numero1 = Fuente.render(str(numeroLlegar), 1, pg.Color("white")) #Fotos, etc

Pantalla.blit(OponenteF, (0, 0))
Pantalla.blit(Numero1, (615, 147))
Pantalla.blit(Numero2, (627, 343))

def imprimir(numeroLlegar,maximoSuma,Oponente):
    if Oponente:
        Pantalla.blit(Computadora, (0, 0))
        Numero1 = Fuente.render(str(numeroLlegar), 1, pg.Color("white"))
        Numero2 = Fuente.render(str(maximoSuma), 1, pg.Color("white"))
        Pantalla.blit(Numero1, (615, 147))
        Pantalla.blit(Numero2, (627, 343))
    else:
        Pantalla.blit(OponenteF, (0, 0))
        Numero1 = Fuente.render(str(numeroLlegar), 1, pg.Color("white"))
        Numero2 = Fuente.render(str(maximoSuma), 1, pg.Color("white"))
        Pantalla.blit(Numero1, (615, 147))
        Pantalla.blit(Numero2, (627, 343))
def imprimir2(Turno,numeroLlegar,maximoSuma,Total,Oponente):
    Pantalla.blit(Fondo2, (0, 0))
    if Oponente == False:
        if Turno:
            Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 60)
            Texto = Fuente.render("TU TURNO", 1,[81,118,163])
            Pantalla.blit(Texto, (100, 335))
        else:
            Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 60)
            Texto = Fuente.render("TURNO COMPUTADORA", 1, [81, 118, 163])
            Pantalla.blit(Texto, (100, 335))
    else:
        if Turno:
            Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 60)
            Texto = Fuente.render("TURNO JUGADOR 1", 1, [81, 118, 163])
            Pantalla.blit(Texto, (100, 335))
        else:
            Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 60)
            Texto = Fuente.render("TURNO JUGADOR 2", 1, [81, 118, 163])
            Pantalla.blit(Texto, (100, 335))
    x = 100
    for numero in range(maximoSuma):
        Pantalla.blit(Cuadrado, (x, 450))
        Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 46)
        NumeroP = Fuente.render(str(numero + 1), 1, pg.Color("white"))
        Pantalla.blit(NumeroP, (x + 30, 467))
        x += 120
    Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 100)
    num = Fuente.render(str(Total), 1, pg.Color("white"))
    Pantalla.blit(num, (230, 90))
    Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 45)
    maxim = Fuente.render('/ '+str(numeroLlegar), 1, pg.Color("white"))
    if Total < 10:
        Pantalla.blit(maxim, (300, 142))
    else:
        Pantalla.blit(maxim, (350, 142))
    pg.display.update()
def inteligencia(numeroL,maximoSuma,Sumas): #numeroL = Numero a llegar; Sumas = lo que va sumando
    listaRestas = []
    totalAux = numeroL #Numero a llegar
    while totalAux > 0:
        listaRestas.append(totalAux)
        totalAux -= maximoSuma + 1 #Le resta el maximo de sumas +1
    for num in reversed(listaRestas): #Busca a que numero debe llegar
        if Sumas < num:
            if num - Sumas > maximoSuma:
                Sumas += randint(1, maximoSuma) #Si el oponente esta en la sucesion suma aleatoriamente
                break
            Sumas += num - Sumas #Si puede llegar a la sucesion le suma lo que le falte
            break
    time.sleep(1)
    return Sumas
def tocoEntre(xy, pos1, pos2):
    if xy == 'x':
        if pg.mouse.get_pos()[0] > pos1 and pg.mouse.get_pos()[0] < pos2:
            return True
        else:
            return False
    elif xy == 'y':
        if pg.mouse.get_pos()[1] > pos1 and pg.mouse.get_pos()[1] < pos2:
            return True
        else:
            return False
def menuInicial(numeroLlegar,maximoSuma,Oponente):#Menu de configuracion, llama a quienEmpieza o jugarOponente
    imprimir(numeroLlegar, maximoSuma, Oponente)
    Terminado = False
    while not Terminado:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type == pg.QUIT:
                pg.quit()
        if pg.mouse.get_pressed()[0]:
            if tocoEntre('y', 157, 194):
                if tocoEntre('x', 506, 546):
                    numeroLlegar -= 1
                    if numeroLlegar == 9:
                        numeroLlegar = 10
                    imprimir(numeroLlegar, maximoSuma, Oponente)
                elif tocoEntre('x', 732, 773):
                    numeroLlegar += 1
                    if numeroLlegar == 100:
                        numeroLlegar = 99
                    imprimir(numeroLlegar, maximoSuma, Oponente)
            elif tocoEntre('y', 357, 391):
                if tocoEntre('x', 506, 546):
                    maximoSuma -= 1
                    if maximoSuma == 1:
                        maximoSuma = 2
                    imprimir(numeroLlegar, maximoSuma, Oponente)
                elif tocoEntre('x', 732, 773):
                    maximoSuma += 1
                    if maximoSuma == 7:
                        maximoSuma = 6
                    imprimir(numeroLlegar, maximoSuma, Oponente)
            elif tocoEntre('y', 509, 562):
                if tocoEntre('x', 483, 522):
                    Oponente = False
                    imprimir(numeroLlegar, maximoSuma, Oponente)
                elif tocoEntre('x', 778, 824):
                    Oponente = True
                    imprimir(numeroLlegar, maximoSuma, Oponente)
            elif tocoEntre('y', 598, 674):
                if tocoEntre('x', 551, 744):
                    if Oponente == True:
                        quienEmpieza(numeroLlegar, maximoSuma, Oponente)
                        Terminado = True
                    else:
                        jugarOponente(True, numeroLlegar, maximoSuma)
            time.sleep(0.05)

        pg.display.update()
        Reloj.tick(fps)
def quienEmpieza(numeroLlegar,maximoSuma,Oponente):# Si juega contra la compu, elige quien empieza. Llama a jugarCompu
    Empezar = False
    Pantalla.blit(EmpiezaC, (0, 0))
    Terminado = False
    while not Terminado:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if tocoEntre('y',381,423):
                    if tocoEntre('x',475,515):
                        imprimir(numeroLlegar,maximoSuma,Oponente)
                        Empezar = True
                        Pantalla.blit(EmpiezoY, (0, 0))
                    elif tocoEntre('x',744,790):
                        imprimir(numeroLlegar,maximoSuma,Oponente)
                        Empezar = False
                        Pantalla.blit(EmpiezaC, (0, 0))
                elif tocoEntre('y',434,491):
                     if tocoEntre('x',565,710):
                        jugarCompu(Empezar,numeroLlegar,maximoSuma)
        pg.display.update()
        Reloj.tick(fps)
def jugarCompu(Empezar,numeroLlegar,maximoSuma): # Juega contra la Computadora. Cuando alguien gana llama a Termino
    Empezar2 = Empezar
    maximoSuma2 = maximoSuma
    Total = 0
    imprimir2(Empezar,numeroLlegar,maximoSuma,Total,Oponente)
    Terminado = False
    while not Terminado:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if tocoEntre('y',198,407):
                    if tocoEntre('x',1000,1203):
                        Total = 0
                        Empezar = Empezar2
                        maximoSuma = maximoSuma2
                if Empezar:
                    if tocoEntre('y',440,543):
                        if tocoEntre('x',99,187):
                            Total += 1
                            Empezar = False
                        elif tocoEntre('x', 220, 310):
                            Total += 2
                            Empezar = False
                        elif tocoEntre('x', 340, 430):
                            if maximoSuma >= 3:
                                 Total += 3
                                 Empezar = False
                        elif tocoEntre('x', 460, 550):
                            if maximoSuma >= 4:
                                 Total += 4
                                 Empezar = False
                        elif tocoEntre('x', 580, 670):
                            if maximoSuma >= 5:
                                Total += 5
                                Empezar = False
                        elif tocoEntre('x', 700, 800):
                            if maximoSuma >= 6:
                                Total += 6
                                Empezar = False
                    if Total + maximoSuma > numeroLlegar:
                        while Total + maximoSuma > numeroLlegar:
                            maximoSuma -=1
                imprimir2(Empezar,numeroLlegar,maximoSuma,Total,Oponente)
        if Total == numeroLlegar:
            if not Empezar:
                termino("Yo",numeroLlegar,maximoSuma2,True,Empezar2)
            else:
                termino("Computadora",numeroLlegar,maximoSuma2,True,Empezar2)
        if not Empezar:
            Total = inteligencia(numeroLlegar,maximoSuma,Total)
            Empezar = True
            if Total + maximoSuma > numeroLlegar:
                while Total + maximoSuma > numeroLlegar:
                    maximoSuma -= 1
            imprimir2(Empezar, numeroLlegar, maximoSuma, Total,Oponente)
        if Total == numeroLlegar:
            if not Empezar:
                termino("Yo",numeroLlegar,maximoSuma2,True,Empezar2)
            else:
                termino("Computadora",numeroLlegar,maximoSuma2,True,Empezar2)
        Reloj.tick(fps)
def jugarOponente(Empezar,numeroLlegar,maximoSuma):
    Empezar2 = Empezar
    maximoSuma2 = maximoSuma
    Total = 0
    imprimir2(Empezar, numeroLlegar, maximoSuma, Total,True)
    Terminado = False
    while not Terminado:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if tocoEntre('y',198,407):
                    if tocoEntre('x',1000,1203):
                        Total = 0
                        Empezar = Empezar2
                        maximoSuma = maximoSuma2
                elif tocoEntre('y', 440, 543):
                    if tocoEntre('x', 99, 187):
                        Total += 1
                        Empezar = not Empezar
                    elif tocoEntre('x', 220, 310):
                        Total += 2
                        Empezar = not Empezar
                    elif tocoEntre('x', 340, 430):
                        if maximoSuma >= 3:
                            Total += 3
                            Empezar = not Empezar
                    elif tocoEntre('x', 460, 550):
                        if maximoSuma >= 4:
                            Total += 4
                            Empezar = not Empezar
                    elif tocoEntre('x', 580, 670):
                        if maximoSuma >= 5:
                            Total += 5
                            Empezar = not Empezar
                    elif tocoEntre('x', 700, 800):
                        if maximoSuma >= 6:
                            Total += 6
                            Empezar = not Empezar
                if Total + maximoSuma > numeroLlegar:
                    while Total + maximoSuma > numeroLlegar:
                        maximoSuma -=1
                imprimir2(Empezar,numeroLlegar,maximoSuma,Total,True)
        if Total == numeroLlegar:
            if not Empezar:
                termino("Jugador 1",numeroLlegar,maximoSuma2,Oponente,Empezar2)
            else:
                termino("Jugador 2",numeroLlegar,maximoSuma2,Oponente,Empezar2)
        if Total == numeroLlegar:
            if not Empezar:
                termino("Jugador 1",numeroLlegar,maximoSuma2,Oponente,Empezar2)
            else:
                termino("Jugador 2",numeroLlegar,maximoSuma2,Oponente,Empezar2)
        Reloj.tick(fps)
def termino(gano,numeroLlegar,maximoSuma,Oponente,Empieza):# vuelve a jugarCompu / jugarOponente o vuelve al menuInicial
    Pantalla.blit(Ganar, (0, 0))
    Fuente = pg.font.Font("/home/alumno/PycharmProjects/Fiorino.Prueba/0.3/Roboto.ttf", 46)
    if gano == "Computadora":
        Ganador = Fuente.render("¡Ganó la computadora!", 1, [34,69,135])
        Pantalla.blit(Ganador, (420, 235))
    elif gano == "Yo":
        Ganador = Fuente.render("¡Ganaste!", 1, [34, 69, 135])
        Pantalla.blit(Ganador, (535, 235))
    elif gano == "Jugador 1":
        Ganador = Fuente.render("¡Ganó el Jugador 1!", 1, [34, 69, 135])
        Pantalla.blit(Ganador, (455, 235))
    elif gano == "Jugador 2":
        Ganador = Fuente.render("¡Ganó el Jugador 2!", 1, [34, 69, 135])
        Pantalla.blit(Ganador, (455, 235))
    Terminado = False
    while not Terminado:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if tocoEntre('y',411,474):
                    if tocoEntre('x',381,571):
                        if Oponente:
                            jugarCompu(Empieza,numeroLlegar,maximoSuma)
                        else:
                            jugarOponente(Empieza,numeroLlegar,maximoSuma)
                    elif tocoEntre('x',690,907):
                        menuInicial(numeroLlegar,maximoSuma,Oponente)
        pg.display.update()
        Reloj.tick(fps)

menuInicial(23,4,False)