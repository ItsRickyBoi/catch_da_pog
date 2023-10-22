import pygame
import random
import math

# Initialize the pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Catch Da Pog")
icon = pygame.image.load('pepe.png')
pygame.display.set_icon(icon)
myfont = pygame.font.SysFont("monospace", 16)

# background image
background = pygame.image.load('catch.png')

# scoring
score = 0

# player
PlayerImg = pygame.image.load('han.png')
playerX = 50
playerY = 275
playerX_change = 0
playerY_change = 0

# Enemy
EnemyImg = pygame.image.load('pog.png')
enemyX = random.randint(700, 744)
enemyY = random.randint(50, 275)
enemyX_change = 5
enemyY_change = 5
enemy_state = "ready"


def enemy(ex, ey):
    global enemy_state
    enemy_state = "ready"
    screen.blit(EnemyImg, (ex, ey))


# drawing player into canvas
def player(x, y):
    screen.blit(PlayerImg, (x, y))


# checking collission
def collides(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt((math.pow(enemyX-playerX, 2)) +
                         (math.pow(enemyY-playerY, 2)))
    if distance < 27:
        return True
    else:
        return False


# check if exit is pressed
running = True
while running:
    # RGB for screen color
    screen.fill((255, 255, 0))
    # background image
    screen.blit(background, (0, 0))
    # scoring
    scoretext = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
    screen.blit(scoretext, (5, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check whether is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
                pygame.key.set_repeat(10, 10)
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
                pygame.key.set_repeat(10, 10)
            if event.key == pygame.K_UP:
                playerY_change = -4
                pygame.key.set_repeat(10, 10)
            if event.key == pygame.K_DOWN:
                playerY_change = 4
                pygame.key.set_repeat(10, 10)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Collission
    collission = collides(playerX, playerY, enemyX, enemyY)
    if collission:
        enemyX = random.randint(700, 744)
        enemyY = random.randint(50, 275)
        score += 100
        print(score)
    else:
        score = score

    # boundaries for enemy
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX = 0
        enemyX_change += 10
    elif enemyX >= 736:
        enemyX = 736
        enemyX_change -= 10

    enemyY += enemyY_change
    if enemyY <= 0:
        enemyY = 0
        enemyY_change += 10
    elif enemyY >= 536:
        enemyY = 536
        enemyY_change -= 10

    # creating boundaries for player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
