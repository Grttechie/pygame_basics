import sys
import pygame
from pygame.locals import *

# initialize pygame
pygame.init()

DISPLAYSURF = pygame.display.set_mode((240,320))
pygame.display.set_caption('Hello World')

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()