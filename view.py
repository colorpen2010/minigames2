import pygame,model
screen=pygame.display.set_mode([800,600])

def ion():
    kote_kyb=pygame.rect.Rect(400,600-128,169,128)
    kote=pygame.image.load('real kartinki/cat1.png')
    if model.show_rects == True:
        kyb=pygame.draw.rect(screen,[0,200,0],kote_kyb,4)


    screen.blit(kote,kote_kyb)

    pygame.display.flip()