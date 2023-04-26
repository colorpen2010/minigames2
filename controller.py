import pygame,model,random
pygame.key.set_repeat(10)
def eve():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type==pygame.KEYDOWN and o.key==pygame.K_LEFT:
            model.control_left()
        if o.type==pygame.KEYDOWN and o.key==pygame.K_RIGHT:
            model.control_right()
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])