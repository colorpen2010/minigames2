import pygame, random

show_rects = False
x = 400
y = 472
katflip = 0
ontroloblak = 0


def oblako_letit():
    global ontroloblak, caplya_kyb

    if oblako_kyb.right >= 800:
        ontroloblak = 1
    if oblako_kyb.left <= 0:
        ontroloblak = 0
    if ontroloblak == 0:
        oblako_kyb.left += 3
    elif ontroloblak == 1:
        oblako_kyb.left -= 3
    caplya_kyb.y += 3
    if caplya_kyb.bottom>=600 or caplya_kyb.colliderect(zatop_kyb) or caplya_kyb.colliderect(water_kyb):
        caplya_kyb.centery=oblako_kyb.centery
        caplya_kyb.centerx= oblako_kyb.centerx
        if zatop_kyb.top>=10:
            zatop_kyb.y-=10
            water_kyb.y -= 10
            water_kyb.height += 10
    if caplya_kyb.colliderect(vedro_kyb):
        caplya_kyb.centery=oblako_kyb.centery
        caplya_kyb.centerx= oblako_kyb.centerx

def control_left():
    global katflip
    if katflip == 1:
        kote_kyb.x += 130
    move_left()
    katflip = 0


def control_right():
    global katflip
    if katflip == 0:
        kote_kyb.x -= 130
    katflip = 1
    move_right()


def move_subjects():
    zontik_kyb.top = kote_kyb.top - 77
    zontik_kyb.right = kote_kyb.right + 22

    vedro_kyb.top = kote_kyb.top - 32
    vedro_kyb.left = kote_kyb.left - 15


def move_left():
    kote_kyb.left -= 3
    if kote_kyb.left <= 18:
        kote_kyb.left = 18
    move_subjects()


def move_right():
    kote_kyb.left += 3
    if kote_kyb.right >= 780:
        kote_kyb.right = 780
    vedro_kyb.top = kote_kyb.top - 32
    zontik_kyb.top = kote_kyb.top - 77
    zontik_kyb.right = kote_kyb.left + 80
    vedro_kyb.left = kote_kyb.right - 50


oblako_kyb = pygame.rect.Rect(50, 50, 150, 100)
kote_kyb = pygame.rect.Rect(x, y, 169, 128)
zontik_kyb = pygame.rect.Rect(0, 0, 102, 102)
vedro_kyb = pygame.rect.Rect(kote_kyb.x - 15, kote_kyb.y - 30, 72, 72)
caplya_kyb = pygame.rect.Rect(oblako_kyb.centerx, oblako_kyb.centery + 20, 20, 40)
zatop_kyb=pygame.rect.Rect(1,570,800,30)
water_kyb=pygame.rect.Rect(zatop_kyb.left,zatop_kyb.bottom,800,0)
move_subjects()
