import pygame,model
def eve():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()

    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])