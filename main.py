import pygame
import time
import sys
import cv2
from PIL import Image as im

# intitalizing pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 800))

#Adding text Intitalization
myfont = pygame.font.SysFont('Comic Sans MS', 30)


# Title and caption
pygame.display.set_caption("Doodler")



isDrawing = False

running = True

screen.fill((255, 255, 255))


drawColor = (0,0,0)

width  = 2



while running:
    
    prev_mouse_x , prev_mouse_y = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN: #Drawing
            if event.key == pygame.K_a:
                isDrawing = True
                drawColor = (0,0,0)
                width = 2

            if event.key == pygame.K_c: #Erasing
                isDrawing = True
                drawColor = (255,255,255)
                width = 34
            
            if event.key == pygame.K_0: #Clear the screen
                screen.fill((255, 255, 255))
                

        if event.type == pygame.KEYUP: #Stop Drawing
            if event.key == pygame.K_a or event.key == pygame.K_c:
                isDrawing =False

    if isDrawing:
        mouse_X , mouse_Y = pygame.mouse.get_pos()
        pygame.draw.line(screen,drawColor,(prev_mouse_x,prev_mouse_y), (mouse_X,mouse_Y), width)






    pygame.display.update()



cv2.destroyAllWindows()
time.sleep(9)
pygame.quit()
sys.exit()
