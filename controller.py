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
            model.solntheistina()
            pygame.time.set_timer(8889, 6000,1)
        if o.type==8889:
            print(6)
            if model.poivles == 1:
                model.poivles=0
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])
