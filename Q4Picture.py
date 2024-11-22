# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('midnightblue'))

# draw a house with a roof
draw.rect(gameDisplay, Color('wheat'), Rect(200, 400, 300, 200))
draw.polygon(gameDisplay, Color('lightpink'), [(200, 300), (300, 300), (150, 100)])

# draw green grass
draw.rect(gameDisplay, Color('wheat'), Rect(10, 300, 400, 100))

# draw a moon
draw.circle(gameDisplay, Color('white'), (300, 350), 50)

# draw a sun
draw.circle(gameDisplay, Color('salmon'), (300, 350), 30)

# draw a star
draw.circle(gameDisplay, Color('brown'), (50, 350), 10)

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")
