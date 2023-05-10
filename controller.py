import pygame, model, random

pygame.key.set_repeat(10)
pygame.time.set_timer(8888, 3000)


def eve():
    events = pygame.event.get()
    for o in events:
        if o.type == 8888:
            model.ontroloblak = random.randint(0, 1)
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_LEFT:
            model.control_left()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_RIGHT:
            model.control_right()
        if o.type==pygame.KEYDOWN and o.key == pygame.K_RETURN:
            if model.poivles==0:
                model.poivles=1
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])
