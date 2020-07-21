import os
import random # to generate random images at any places every time
import game_config as gc # to use all the variables we have created

from pygame import image,transform

# for this class we have to create a dictionary for each animal count to display image only twice 
animals_count = dict((a,0) for a in gc.ASSET_FILES)  # initially each count will be zero 0

# creating a function of available animals awhich will return a list of available animals to be displayed

def available_animals():
  return [a for a,c in animals_count.items() if c<2]

#let's define the main animal class

class animal:
  def __init__(self,index):
    # we passed a index associated with each animal this will from 0-15(inclusive) because there are 16 images total
    #on the basis of indexc we'll places the animal on the game board
    self.index = index
    self.row = index // gc.NUM_TILES_SIDE # it will be helpful to access the indexx with row in later
    self.column = index % gc.NUM_TILES_SIDE
    
    #let's create a association of name with index randomly
    
    self.name = random.choice(available_animals())
    #now we have to update the dictionary 
    
    animals_count[self.name] +=1
    
    #to associate image path with name 
    self.image_path = os.path.join(gc.ASSET_DIR, self.name)
    self.image = image.load(self.image_path)

    #it will resize our image as required
    self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN)) 
    
    # we have to create a box to hide the image 
    self.box = self.image.copy()
    
    #filling to this box
    self.box.fill((200,200,200)) #gray color 
    
    # a boolean to be used in 
    self.skip = False
    
