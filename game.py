import pygame #importing the main library we'll going to use
from pygame import display, event  #importing two subpackage for our game one for takng input and other for displaying it
#for displaying image we have to import image module 
from pygame import image 

pygame.init() #this initialization is important to be done before using any of the functionality

display.set_caption ("My Game: FLIP AND MATCH") # here we can give a title to our game

#Now set mode function creates(returns) a surface object for our 
#game anything we want to display on main game screen will be set to this screen object

screen = display.set_mode((512,512)) 

#creating a screen element of matched png to be dislpayed later
matched = image.load('otherassets/matched.png')

#this will only create a element but to display that image we have to blit the image using blit function

screen.blit(matched, (0,0,512,512)) #second arguement is a tuple of coordinated upperleft to lowerright
#as we want it on whole window we are taking 512 
#now even the image has been set but we didn't displayed it yet so for displaying we have to call flip method

display.flip()

#let's set a boolean variable and called it running 
running = True 

#we'll iterate over game loop untill this variable is true

#Now simply creating a game loop 
# which will be a while loop 
while running:
  # pygame module provides us a get() function in events which fetches all the event as queue 
  # and returns a list of keyboard and mouse event 
  # and after the next call to this function this list renewed
  current_events = event.get()
  
  # iterating over the list of events with for loops
  for e in current_events:
    if e.type == QUIT:
      running = False
      

  
