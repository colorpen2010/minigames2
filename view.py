import pygame,model
screen=pygame.display.set_mode([800,600])

kote = pygame.image.load('real kartinki/cat1.png')
zontik = pygame.image.load('real kartinki/umbrella.png')
vedro = pygame.image.load('real kartinki/bucket.png')
oblako=pygame.image.load('real kartinki/cloud.png')
caplya=pygame.image.load('real kartinki/water_drop.png')
zatoplenie=pygame.image.load('real kartinki/water.png')


zontik = pygame.transform.scale(zontik, [100, 100])

vedro = pygame.transform.scale(vedro, [70, 70])

oblako=pygame.transform.scale(oblako,model.oblako_kyb.size)

caplya=pygame.transform.scale(caplya,model.caplya_kyb.size)

zatoplenie=pygame.transform.scale(zatoplenie,model.zatop_kyb.size)



def ion():
    global kote
    screen.fill([0,0,0])

    if model.katflip==1:
        kote2i0=pygame.transform.flip(kote,True,False)
        zontik2i0=pygame.transform.flip(zontik,True,False)
        vedro2i0=pygame.transform.flip(vedro,True,False)
        screen.blit(kote2i0,model.kote_kyb)
        screen.blit(zontik2i0, model.zontik_kyb)
        screen.blit(vedro2i0, model.vedro_kyb)

    if model.katflip==0:
        screen.blit(kote,model.kote_kyb)
        screen.blit(zontik,model.zontik_kyb)
        screen.blit(vedro,model.vedro_kyb)
    screen.blit(zatoplenie,model.zatop_kyb)
    screen.blit(caplya,model.caplya_kyb)
    screen.blit(oblako,model.oblako_kyb)
    water=pygame.draw.rect(screen,[52,144,193],model.water_kyb)

    if model.show_rects == True:
        pygame.draw.rect(screen,[0,200,0],model.kote_kyb,4)
        zonkyb = pygame.draw.rect(screen, [200,0, 0], model.zontik_kyb, 4)
        vedrokyb = pygame.draw.rect(screen, [100,50,0], model.vedro_kyb, 4)
        oblakokyb=pygame.draw.rect(screen,[244,233,255],model.oblako_kyb,4)
        caplyakyb=pygame.draw.rect(screen,[10,10,255],model.caplya_kyb,4)
        zatopleniekyb=pygame.draw.rect(screen,[50,10,200],model.zatop_kyb,4)
        waterkyb = pygame.draw.rect(screen, [0, 0, 30], model.water_kyb,4)

    pygame.display.flip()