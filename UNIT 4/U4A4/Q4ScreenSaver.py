import pygame
from pygame import Color, draw, display, time, Rect


pygame.init()

clock = time.Clock()
pygame.display.set_caption("Save Screen")

gameDisplay = pygame.display.set_mode((600,400))
gameDisplay.fill(Color('white'))

x = 150
y = 250
x1 = 250
y1 = 310
x2 = 100
y2 = 190
x3 = 200
y3 = 260
x4 = 170
y4 = 270
counter = 0

while counter < 4:
  for i in range(27):
    gameDisplay.fill(Color('white'))
    draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
    draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
    draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
    draw.circle(gameDisplay, Color('white'), (x,y), (14))
    draw.circle(gameDisplay, Color('black'), (x,y), (7))
    display.flip()
    x = x + i
    x1 = x1 + i
    x2 = x2 + i
    x3 = x3 + i
    x4 = x4 + i
    clock.tick(10)
  for i in range(20):
    gameDisplay.fill(Color('white'))
    draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
    draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
    draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
    draw.circle(gameDisplay, Color('white'), (x,y), (14))
    draw.circle(gameDisplay, Color('black'), (x,y), (7))
    display.flip()
    y = y - i
    y1 = y1 - i
    y2 = y2 - i
    y3 = y3 - i
    y4 = y4 - i
    clock.tick(10)
    display.flip()
  for i in range(25):
    gameDisplay.fill(Color('white'))
    draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
    draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
    draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
    draw.circle(gameDisplay, Color('white'), (x,y), (14))
    draw.circle(gameDisplay, Color('black'), (x,y), (7))
    display.flip()
    y = y + i
    y1 = y1 + i
    y2 = y2 + i
    y3 = y3 + i
    y4 = y4 + i
    x = x - i
    x1 = x1 - i
    x2 = x2 - i
    x3 = x3 - i
    x4 = x4 - i
    clock.tick(10)
    display.flip()
    counter = counter + 1