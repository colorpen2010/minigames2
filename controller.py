import pygame,model,random
pygame.key.set_repeat(10)
def eve():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type==pygame.KEYDOWN and o.key==pygame.K_LEFT:
            model.x-=3
        if o.type==pygame.KEYDOWN and o.key==pygame.K_RIGHT:
            model.x+=3

    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])