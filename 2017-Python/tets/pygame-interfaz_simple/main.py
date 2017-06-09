import pygame

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([500 , 500])
    pygame.display.set_caption("seba y alessa y ese chico de color que me esta mirando")
    salir = False
    reloj = pygame.time.Clock()
    blanco = (255,255,255)
    rojo = (255,0,0)
    azul = (0,0,255)
    verde = (0, 255, 0)
    color_loco = (120, 84, 100)
    s1 = pygame.Surface((100, 60))
    s1.fill(rojo)
    s2 = pygame.Surface((100, 150))
    s2.fill(azul)

    r1 = pygame.Rect(10, 10, 480, 30)
    r2 = pygame.Rect(10, 45, 200, 300)
    r3 = pygame.Rect(50, 50, 10, 10)

    while salir != True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                salir = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                r1.move_ip (5 , 5)
                pygame.mouse.set_pos (150 , 150)
                if r3.colliderect(r2):
                    r2.height = 10
                    r2.width = 10
            #if evento.type == pygame.MOUSEMOTION:
            #    r1.move_ip (-1 , -1)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    r3.move_ip (0 , 15)
                if evento.key == pygame.K_UP:
                    r3.move_ip (0 , -15)
                if evento.key == pygame.K_LEFT:
                    r3.move_ip (-15 , 0)
                if evento.key == pygame.K_RIGHT:
                    r3.move_ip (15 , 0)



        #x = 0
        #while x < 100:
        #    pygame.display.update()
        #    pantalla.blit(s1, [x, 0])
        #    x += 5
        #    s1.fill(azul)
        #    pantalla.blit(s1, [x, 0])
        #    pygame.display.update()
        #    x += 5
        #   s1.fill(rojo)
        #   reloj.tick(1)

        #pantalla.blit(s1, [0, 0])
        #pantalla.blit(s2, [80, 110])

        reloj.tick(60)
        pantalla.fill (blanco)
        #(xant , yant) = (r3.left , r3.top)
        (r3.left , r3.top) = pygame.mouse.get_pos()
        r3.left -= r3.width / 2
        r3.top -= r3.height / 2
        #if (r3.colliderect(r2)):
            #(r3.left , r3.top) = (xant , yant)
            #r2.inflate_ip (1 , 1)
        pygame.draw.rect(pantalla , verde , r1)
        pygame.draw.rect(pantalla , azul , r2)
        pygame.draw.rect(pantalla , color_loco , r3)
        pygame.display.update()
main()