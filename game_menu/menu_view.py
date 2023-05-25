import pygame, menu_model
pygame.init()

h = pygame.font.SysFont('arial', 25, True, True)

fonar1 = 250
fonar2 = 0
fonar3 = 0

fon = pygame.image.load('menu_kartinki/fon.jpg')
fon2 = pygame.image.load('menu_kartinki/fon2.jpg')
fon3 = pygame.image.load('menu_kartinki/fon3.jpg')

icon = pygame.image.load('menu_kartinki/icon.png')



screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Menu')
pygame.display.set_icon(icon)

fon = pygame.transform.scale(fon, [500, 500])
fon2 = pygame.transform.scale(fon2, [500, 500])
fon3 = pygame.transform.scale(fon3, [500, 500])
fon0 = fon.convert_alpha()
fon_1 = fon2.convert_alpha()
fon_2 = fon3.convert_alpha()

d = h.render('игра поймай воду', True, [55, 25, 20])

def viewer():
    global fonar1, fonar2, fonar3
    if menu_model.fonario == 0:
        if fonar2 >= 0:
            fonar2 -= 0.5
        if fonar1 <= 250:
            fonar1 += 0.5
        if fonar3 >= 0:
            fonar3 -= 0.5
        fon0.set_alpha(fonar1)
        fon_1.set_alpha(fonar2)
        fon_2.set_alpha(fonar3)

    if menu_model.fonario == 1:
        if fonar2 <= 255:
            fonar2 += 0.5
        if fonar1 >= 0:
            fonar1 -= 0.5
        if fonar3 >= 0:
            fonar3 -= 0.5
        fon0.set_alpha(fonar1)
        fon_1.set_alpha(fonar2)
        fon_2.set_alpha(fonar3)

    if menu_model.fonario == 2:
        if fonar2 >= 0:
            fonar2 -= 0.5
        if fonar1 >= 0:
            fonar1 -= 0.5
        if fonar3 <= 255:
            fonar3 += 0.5
        fon0.set_alpha(fonar1)
        fon_1.set_alpha(fonar2)
        fon_2.set_alpha(fonar3)

    screen.fill([255, 255, 255, 255])
    screen.blit(fon0, [0, 0])
    screen.blit(fon_1, [0, 0])
    screen.blit(fon_2, [0, 0])

    pygame.draw.rect(screen, [57, 68, 100], menu_model.button1)
    screen.blit(d,[menu_model.button1.left+5,menu_model.button1.top])

    pygame.display.flip()
