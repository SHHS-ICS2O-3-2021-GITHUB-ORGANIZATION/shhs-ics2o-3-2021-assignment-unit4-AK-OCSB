
import pygame
from pygame import Color, Rect, draw, time

#Tutorial
#x = pygame.init()
#print(x)

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Slither")


pygame.display.update()

gameExit = False
lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0

lead_y_change = 0

clock = pygame.time.Clock()
block_size = 10
FPS = 15

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


def gameLoop():
    gameExit = False
    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(Color('white'))
            message_to_screen("Game Over, press c to play again or q to quit" , Color('red'))
            pygame.display.update()
            
            for even in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        
        
        
        
        
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
              lead_x_change = -block_size
              lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
              lead_x_change = block_size
              lead_y_change = 0
    
            elif event.key == pygame.K_UP:
              lead_y_change = -block_size
              lead_x_change = 0
            elif event.key == pygame.K_DOWN:
              lead_y_change = block_size
              lead_x_change = 0
              
              
      if lead_x >= display_width  or lead_x < 0 or lead_y >= display_height or lead_y < 0:
          gameExit = True
          
            
      lead_x += lead_x_change
      lead_y += lead_y_change    
    
    
      gameDisplay.fill(Color('white'))
      pygame.draw.rect(gameDisplay, Color('black'), [lead_x, lead_y,block_size,block_size])
        
    
      pygame.display.update()
      clock.tick(FPS)
       pygame.display.update()

    pygame.quit()
    quit()
    
gameLoop()