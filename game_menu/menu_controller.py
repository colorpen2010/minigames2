import pygame,menu_model
t=pygame.event.custom_type()
pygame.time.set_timer(t, 30000)

def conter():
    events=pygame.event.get()
    for o in events:
        if o.type ==t:
            if menu_model.fonario==2:
                menu_model.fonario=0
            elif menu_model.fonario==0:
                menu_model.fonario=1
            elif menu_model.fonario==1:
                menu_model.fonario=2
        if o.type==pygame.MOUSEBUTTONDOWN:
            if menu_model.button1.collidepoint(o.pos[0],o.pos[1]):
                print(o.pos)
        if o.type==pygame.QUIT:
            exit()