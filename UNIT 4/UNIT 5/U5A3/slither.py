import pygame
from pygame import Color, Rect, draw, time

#Tutorial
#x = pygame.init()
#print(x)

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Slither")


pygame.display.update()

gameExit = False
lead_x = 300
lead_y = 300
lead_x_change = 0
clock = pygame.time.Clock()
lead_y_change = 0


while not gameExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      gameExit = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          lead_x_change = -10
          lead_y_change = 0
        elif event.key == pygame.K_RIGHT:
          lead_x_change = 10
          lead_y_change = 0

        elif event.key == pygame.K_UP:
          lead_y_change = -10
          lead_x_change = 0
        elif event.key == pygame.K_DOWN:
          lead_y_change = 10
          lead_x_change = 0
    
        
  lead_x += lead_x_change
  lead_y += lead_y_change    


  gameDisplay.fill(Color('white'))
  pygame.draw.rect(gameDisplay, Color('black'), [lead_x, lead_y,10,10])
    

  pygame.display.update()
  clock.tick(15)

pygame.quit()
quit()