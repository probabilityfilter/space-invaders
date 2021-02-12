import pygame
import os
import time
import random

CURRENT_PATH = os.path.dirname("Users\ArunRamamoorthy\Documents\Python Scripts\space invaders\\assets\pixel_ship_red_small.png") 
print(type(CURRENT_PATH))
print(CURRENT_PATH) 
#LOAD IMAGES
# print(os.path.join("assets", "pixel_ship_red_small.png"))
# redSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
# redSpaceShip = pygame.image.load('pixel_ship_red_small.png')
redSpaceShip = pygame.image.load(os.path.join("Users\ArunRamamoorthy\Documents\Python Scripts\space invaders\assets", "pixel_ship_red_small.png"))

# greenSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
# blueSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
# yellowSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# redLaser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
# greenLaser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
# blueLaser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
# yellowLaser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# bg = pygame.image.load(os.path.join("assets", "background-black.png"))