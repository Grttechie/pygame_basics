import pygame
import sys

from pygame.locals import *

# initialize pygame
pygame.init()

''' In pygame, we represent colors as a tuple of three(3) integers.
For example: (R,G,B)
R = Red Value (0 to 255)
G = Green Value (0 to 255)
B = Blue Value (0 to 255)
'''

# color variables
Aqua = ( 0, 255, 255)
Black = ( 0, 0, 0)
Blue = ( 0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = ( 0, 128, 0)
Lime = ( 0, 255, 0)
Maroon = (128, 0, 0)
Navy_Blue = ( 0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = ( 0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)

# Transparent Colors
# (R,G,B,A) A is the Alpha value (How opaque the color is) from 0 to 255
# A = 0 (Completely transparent)
# A = 255 (Not transparent)

# ANOTHER WAY TO DISPLAY A COLOR
trans_red = pygame.Color(255,0,0,25)


# create a surface object
DISPLAYSURF = pygame.display.set_mode((500,400))

# create another surface object for transparent colors to be drawn on
TRANS_COLOR_SURF = DISPLAYSURF.convert_alpha()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # uninitialize the pygame module
            pygame.quit()
            sys.exit()
    
    # update the surface object on the screen
    pygame.display.update()