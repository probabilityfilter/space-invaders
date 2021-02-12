import pygame
import os
import time
import random

wd,ht = 750,750
win = pygame.display.set_mode((wd,ht)) #it's a tuple
pygame.display.set_caption("Space Invaders")

#LOAD IMAGES
redSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
greenSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
blueSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#PLAYER SHIP
yellowSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

redLaser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
greenLaser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blueLaser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellowLaser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

bg = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                