import pygame
import sys

from pygame.locals import *

# initialize the pygame module
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))

'''There are two ways to represent a rect object in pygame:
1. Tuples of 4 integers: (X, Y, width, height)
2. Using the Rect Object: pygame.Rect(X, Y, width, height)
'''

rect1 = (10,30,50,50)
rect2 = pygame.Rect(20,40,60,80)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()