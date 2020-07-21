import pygame #importing the main library we'll going to use
from pygame import display, event  #importing two subpackage for our game one for takng input and other for displaying it
#for displaying image we have to import image module 
from pygame import image 
from Animal import Animal
from time import sleep # to stop for a while when image matches


pygame.init() #this initialization is important to be done before using any of the functionality

display.set_caption ("My Game: FLIP AND MATCH") # here we can give a title to our game

#Now set mode function creates(returns) a surface object for our 
#game anything we want to display on main game screen will be set to this screen object

screen = display.set_mode((512,512)) 

#creating a screen element of matched png to be dislpayed later
matched = image.load('otherassets/matched.png')

#this will only create a element but to display that image we have to blit the image using blit function

#screen.blit(matched, (0,0,512,512)) #second arguement is a tuple of coordinated upperleft to lowerright
#as we want it on whole window we are taking 512 
#now even the image has been set but we didn't displayed it yet so for displaying we have to call flip method

#display.flip()
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
#let's set a boolean variable and called it running 
running = True 

def find_index(x,y):
  row = x//gc.IMAGE_SIZE
  col = y//gc.IMAGE_SIZE
  
  index = row*gc.NUM_TILES_SIDE + col
  
  return index
#we'll iterate over game loop untill this variable is true
#Now simply creating a game loop 
# which will be a while loop 
total_skipped = 0  # for finishing the game when each image matched
while running:
  # pygame module provides us a get() function in events which fetches all the event as queue 
  # and returns a list of keyboard and mouse event 
  # and after the next call to this function this list renewed
  current_events = event.get()
  
  # iterating over the list of events with for loops
  for e in current_events:
    if e.type == QUIT:
      running = False
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        running = False
    if e.type == pygame.MOUSEBUTTONDOWN:
      #now we have to find the position of mouse to access index
      #once we have index then we can handle it
      mouse_x,mouse_y = pygame.mouse.get_pos()
      #print(mouse_x,mouse_y)
      index = find_index(mouse_x,mouse_y)
      #print(index)
      #let's create a list of current_images to be displayed 
      if index not in current_images:
        current_images.append(index)
      if len(current_images) > 2:
        current_images = current_images[1:]
        
      
      
  #first of all create a blank white background
  screen.fill(255,255,255)
   
  #displaying  each image randomly
  for _,tile in enumerate(tiles):
    #this is because we only wants 2 image at a time
    image_i = tile.image if tile.index in current_images else tile.box 
    if not tile.skip:
      screen.blit(image_i, (tile.col*gc.IMAGE_SIZE+gc.MARGIN, tile.row*gc.IMAGE_SIZE+gc.MARGIN))
    else :
      total_skipped +=1
     
  if len(current_images) == 2:
    idx1,idx2 = current_images
    if tiles[idx1].name == tiles[idx2].name:
      tiles[idx1].skip = True
      tiles[idx2].skip = True
      sleep(0.4)
      screen.blit(matched, (0,0))
      display.flip()
      sleep(0.4)
      current_images = []
    
  if total_skipped == len(tiles): #or we can say 16 here means we will finish the Game when all are matched
    running = False
     
  
  #we must have to flip this tile to display image 
  display.flip()
    
   
  
