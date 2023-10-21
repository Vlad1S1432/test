import pygame
import time
import sys
from random import randint
pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(400,400,50,50)
player_image_orig = pygame.image.load('cat.jpg')
player_img = pygame.transform.scale(player_image_orig,(player.width,player.height))

enemy = pygame.Rect(50,50,30,30)
enemy_img = pygame.image.load('creeper.png')
enemy_img = pygame.transform.scale(enemy_img,(enemy.width,enemy.height))

direction = 'none'

while True:
    screen.fill((66,90,67))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
        elif event.type == pygame.KEYUP:
                direction = 'none'
    if direction == 'left':
        player.x -= 3
    if direction == 'right':
        player.x += 3
    if direction == 'up':
        player.y -= 3
    if direction == 'down':
        player.y += 3

    if player.colliderect(enemy):
        enemy.x = randint(0,470)
        enemy.y = randint(0, 470)
        player.width  += 5
        player.height += 5
        player_img = pygame.transform.scale(player_image_orig,(player.width,player.height))
    screen.blit(player_img,player)
    screen.blit(enemy_img, enemy)
    pygame.display.update()
    clock.tick(60)