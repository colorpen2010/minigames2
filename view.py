import pygame,model
screen=pygame.display.set_mode([800,600])

kote = pygame.image.load('real kartinki/cat1.png')
zontik = pygame.image.load('real kartinki/umbrella.png')
vedro = pygame.image.load('real kartinki/bucket.png')

zontik = pygame.transform.scale(zontik, [100, 100])

vedro = pygame.transform.scale(vedro, [70, 70])

def ion():
    screen.fill([0,0,0])
    if model.show_rects == True:
        kyb=pygame.draw.rect(screen,[0,200,0],model.kote_kyb,4)
        zonkyb = pygame.draw.rect(screen, [200,0, 0], model.zontik_kyb, 4)
        vedrokyb = pygame.draw.rect(screen, [100,50,0], model.vedro_kyb, 4)


    screen.blit(kote,model.kote_kyb)
    screen.blit(zontik,model.zontik_kyb)
    screen.blit(vedro,model.vedro_kyb)

    pygame.display.flip()