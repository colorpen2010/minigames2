import pygame

fon=pygame.image.load('menu_kartinki/fon.jpg')
icon=pygame.image.load('menu_kartinki/icon.png')

button1=pygame.rect.Rect(50,350,200,80)

screen=pygame.display.set_mode([500,500])
pygame.display.set_caption('Menu')
pygame.display.set_icon(icon)


fon=pygame.transform.scale(fon,[500,500])
def viewer():
    screen.blit(fon,[0,0])

    pygame.draw.rect(screen,[57,68,100],button1)

    pygame.display.flip()