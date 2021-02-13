import pygame
import os
import time
import random
pygame.font.init()

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

bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (wd,ht))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        # pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 100))
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = yellowSpaceShip
        self.laser_img = yellowLaser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    color_map = {
                "red": (redSpaceShip, redLaser),
                "green": (greenSpaceShip, greenLaser),
                "blue": (blueSpaceShip, blueLaser),
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.color_map[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
    
    def move(self, vel):
        self.y += vel

def main():
    run = True
    fps = 60
    level = 0
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1
    
    player_vel = 5
    
    player = Player(300,650)

    clock = pygame.time.Clock()

    lost = False

    def redraw_window():
        win.blit(bg, (0,0))
        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        win.blit(lives_label, (10, 10))
        win.blit(level_label, (wd - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(win)
        player.draw(win)

        pygame.display.update()

    while run:
        clock.tick(fps)

        if lives <= 0 or player.health <= 0:
            lost = True

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, wd-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: #left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < wd: #right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0: #up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < ht: #down
            player.y += player_vel

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > ht:
                lives -= 1
                enemies.remove(enemy)

        redraw_window()
main()