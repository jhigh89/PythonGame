import pygame

# starting up pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Caption Icon displayed on screen
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player stuff
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

def player ():
    screen.blit(playerImg,(playerX,playerY))


# loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background color of screen
    screen.fill((0,0,0))

    player()
    pygame.display.update()
