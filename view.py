import pygame,model
screen=pygame.display.set_mode([800,600])

def ion():
    screen.fill([0,0,0])
    kote_kyb=pygame.rect.Rect(model.x, model.y, 169, 128)
    kote=pygame.image.load('real kartinki/cat1.png')

    zontik_kyb=pygame.rect.Rect(kote_kyb.x+75,kote_kyb.y-77,102,102)
    zontik=pygame.image.load('real kartinki/umbrella.png')
    zontik=pygame.transform.scale(zontik,[100,100])

    vedro_kyb=pygame.rect.Rect(kote_kyb.x-15,kote_kyb.y-30,72,72)
    vedro=pygame.image.load('real kartinki/bucket.png')
    vedro=pygame.transform.scale(vedro,[70,70])

    if model.show_rects == True:
        kyb=pygame.draw.rect(screen,[0,200,0],kote_kyb,4)
        zonkyb = pygame.draw.rect(screen, [200,0, 0], zontik_kyb, 4)
        vedrokyb = pygame.draw.rect(screen, [100,50,0], vedro_kyb, 4)


    screen.blit(kote,kote_kyb)
    screen.blit(zontik,zontik_kyb)
    screen.blit(vedro,vedro_kyb)

    pygame.display.flip()