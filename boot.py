import pygame, sys, time, threading
from pygame.locals import MOUSEBUTTONDOWN

def boot():
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption("FreeCreate v0.001")
    screen.fill((0, 0, 0))
    
    picList = ["NNS图标2.png", "python2.png", "FreeCreate 2.png"]
    imgList = []
    for i in picList:
        myImage = pygame.image.load(i).convert()
        imgList.append(myImage)
        
    imgNum = 0
    image = imgList[imgNum]
    a = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = 0
                imgNum += 1
                if imgNum > len(imgList) - 1:
                    pygame.quit()
                    return
        image = imgList[imgNum]
        a = a + 1
        if a > 255:
            a = 0
        image.set_alpha(a)
        screen.fill((0, 0, 0))
        screen.blit(image, (0, 0))
        '''screen.blit(FreeCreateImg, (0, 0))'''

        pygame.display.update()
        time.sleep(0.01)
