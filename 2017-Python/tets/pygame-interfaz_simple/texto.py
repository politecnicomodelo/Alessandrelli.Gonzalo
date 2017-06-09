import pygame


# importo el modulo


# funcion main
def main():
    pygame.init()  # inicializo el modulo

    # fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
    pantalla = pygame.display.set_mode((300, 300))

    pygame.display.set_caption("Mi Ventana")  # Titulo de la Ventana
    # creo un reloj para controlar los fps
    reloj1 = pygame.time.Clock()
    fuente_1 = pygame.font.Font(None , 48)

    blanco = (255, 255, 255)  # color blanco en RGB
    negro = (0, 0, 0)
    texto = fuente_1.render("SEBA lindo" , 0 , (negro))

    salir = False
    # LOOP PRINCIPAL
    while salir != True:
        # recorro todos los eventos producidos
        # en realidad es una lista
        for event in pygame.event.get():
            # si el evento es del tipo
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir = True

        reloj1.tick(20)  # operacion para que todo corra a 20fps
        pantalla.fill(blanco)  # pinto la superficie de blanco
        pantalla.blit(texto , (50 , 50))

        pygame.display.update()  # actualizo el display

    pygame.quit()


main() #vamos por el capitulo 15