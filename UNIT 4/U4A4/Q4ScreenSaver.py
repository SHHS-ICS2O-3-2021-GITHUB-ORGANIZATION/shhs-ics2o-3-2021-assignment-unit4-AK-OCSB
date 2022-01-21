#NAME OF AUTHOR: ASHLEY KOZA
#NAME OF PROGRAM: Q4ScreenSaver
#DATE OF CREATION: 2022-01-18
#PURPOSE OF PROGRAM: Practice pygame modules and how to move around shapes on pygame.




import pygame
from pygame import Color, draw, display, time

#Initialize pygame modules
pygame.init()

clock = time.Clock()

#Title pygame program
pygame.display.set_caption("Screen Saver")

#Get a surface for graphics display
gameDisplay = pygame.display.set_mode((600,400))


#X Varibles
x = 150
x1 = 250
x2 = 100
x3 = 200
x4 = 170

#Y Varibles
y = 250
y1 = 310
y2 = 190
y3 = 260
y4 = 270

#While loop varible
counter = 0

#Loops twice
while counter < 2:
  
  #Increasing Counter
  counter = counter + 1
  
  
  for i in range(27):
    
   
    #White background
    gameDisplay.fill(Color('white'))
    
    #Draw fishes body
    draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
    draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
    
    #Draw fishes fins
    draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
    
    #Draw fishes eyes
    draw.circle(gameDisplay, Color('white'), (x,y), (14))
    draw.circle(gameDisplay, Color('black'), (x,y), (7))
    
    #shows the graphics on the screen
    display.flip()
    
    #Moves all shapes(images)right
    x = x + i
    x1 = x1 + i
    x2 = x2 + i
    x3 = x3 + i
    x4 = x4 + i
    
    #Delays program-10 frames per second
    clock.tick(10)
    
    
  for i in range(20):
    
    
    #White background
    gameDisplay.fill(Color('white'))
    
    #Draw fishes body
    draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
    draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
    
    #Draw fishes fins
    draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
    
    #Draw fishes eyes
    draw.circle(gameDisplay, Color('white'), (x,y), (14))
    draw.circle(gameDisplay, Color('black'), (x,y), (7))
    
     #shows the graphics on the screen
    display.flip()
    
    
    #Moves all shapes(images)up
    y = y - i
    y1 = y1 - i
    y2 = y2 - i
    y3 = y3 - i
    y4 = y4 - i
    
    
    #Delays program-10 frames per second
    clock.tick(10)
    
    
  for i in range(20):
    
    #White background
    gameDisplay.fill(Color('white'))
    
    #Draw fishes body
    draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
    draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
    
    #Draw fishes fins
    draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
    
    #Draw fishes eyes
    draw.circle(gameDisplay, Color('white'), (x,y), (14))
    draw.circle(gameDisplay, Color('black'), (x,y), (7))
    
    #shows the graphics on the screen
    display.flip()
    
    #Moves all shapes(images)down
    y = y + i 
    y1 = y1 + i
    y2 = y2 + i
    y3 = y3 + i
    y4 = y4 + i
    
    #Moves all shapes(images)left at the same time as moving images down
    x = x - i -  13
    x1 = x1 - i - 13 
    x2 = x2 - i  -13
    x3 = x3 - i  - 13
    x4 = x4 - i  - 13
    
    #Delays program-10 frames per second
    clock.tick(10)
    
    
for i in range(20):
  
  
  #White background
  gameDisplay.fill(Color('white'))
  
  #Draw fishes body
  draw.polygon(gameDisplay, Color('orange'), [(x, y), (x1,y1), (x1,y2)])
  draw.polygon(gameDisplay, Color('yellow'), [(x2, y), (x3,y1), (x3,y2)])
  
  #Draw fishes fin
  draw.polygon(gameDisplay, Color('green'), [(x3, y3), (x4,y4), (x4,y)])
  
  #Draw fishes eyes
  draw.circle(gameDisplay, Color('white'), (x,y), (14))
  draw.circle(gameDisplay, Color('black'), (x,y), (7))
  
  #shows the graphics on the screen
  display.flip()
  
  #Moves all shapes(images)right
  x = x + i
  x1 = x1 + i 
  x2 = x2 + i
  x3 = x3 + i 
  x4 = x4 + i  
  
  #Delays program-10 frames per second
  clock.tick(10)
  
  #Unitilize pygame-Not working on replit so commented out
  #pygame.quit()

  #Exit out of python-Not working on replit so commented out
  #quit()
