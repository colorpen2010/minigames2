import pygame,random
show_rects=False
x=400
y=472

def move_subjects():
    zontik_kyb.top=kote_kyb.top-77
    zontik_kyb.right=kote_kyb.right+22

    vedro_kyb.top=kote_kyb.top-32
    vedro_kyb.left=kote_kyb.left-15

def move_left():
    kote_kyb.left-=3
    if kote_kyb.left<=18:
        kote_kyb.left=18
    move_subjects()

def move_right():
    kote_kyb.left+=3
    move_subjects()

kote_kyb = pygame.rect.Rect(x, y, 169, 128)
zontik_kyb = pygame.rect.Rect(0, 0, 102, 102)
vedro_kyb = pygame.rect.Rect(kote_kyb.x - 15, kote_kyb.y - 30, 72, 72)
move_subjects()