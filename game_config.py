import os # here we're going to interact with operating system 

#setting a screen size of 128 because we had already created a screen object of 512 size and 
#there will be 4 images in a line
IMAGE_SIZE = 128 

#setting a screen size equal to screen object we created
SCREEN_SIZE = 512

#number of tiles in a line
NUM_TILES_SIDE = 4

#number of total tiles
NUM_TILES_TOTAL = 16

#margin between tiles
MARGIN = 4

#accessing the images from assets directory 
#through interacting with operating system using os library
ASSET_DIR = 'assets'

#creating a list of images file based on that if the format is png
#because we'll going to iterate over this later
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']

