import pygame,model
screen=pygame.display.set_mode([800,600])

def ion():
    kote_kyb=pygame.rect.Rect(400,600-128,169,128)
    kote=pygame.image.load('real kartinki/cat1.png')

    zontik_kyb=pygame.rect.Rect(475,395,102,102)
    zontik=pygame.image.load('real kartinki/umbrella.png')
    zontik=pygame.transform.scale(zontik,[100,100])
    if model.show_rects == True:
        kyb=pygame.draw.rect(screen,[0,200,0],kote_kyb,4)
        zonkyb = pygame.draw.rect(screen, [200,0, 0], zontik_kyb, 4)


    screen.blit(kote,kote_kyb)
    screen.blit(zontik,zontik_kyb)

    pygame.display.flip()