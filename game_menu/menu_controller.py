import pygame
def conter():
    events=pygame.event.get()
    for o in events:
        if o.type==pygame.QUIT:
            exit()