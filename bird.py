import pygame, sys
from pygame.locals import *
import random
import math
from pygame import mixer

# initialize pygame
pygame.init()


# Create the screen
clock = pygame.time.Clock()

screen = pygame.display.set_mode((280, 511))

# Create background
background = pygame.image.load('bg.png')
floor_surface = pygame.image.load('base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floorX = 0


# Background sound
#mixer.music.load('background.wav')
#mixer.music.play(-1)

# Game Over Text
#over_font = pygame.font.Font('freesansbold.ttf',68)

# title and icon
pygame.display.set_caption("FLAPPY BIRD")
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)


# Adding player
playerImg = pygame.image.load('bird.png').convert_alpha()
playerX = 10
playerY = 190
playerX_change = 0

# adding pipes
pipe_surface = pygame.image.load('pipe.png')

pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [300,400,500]

# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
#score = 0
#high_score = 0

def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (x,y))

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (440, 255))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-= 3.5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

def draw_floor():
    screen.blit(floor_surface, (floorX, 420))
    screen.blit(floor_surface, (floorX +276,420))




# Game loop
run = True
while run:

    clock.tick(120)

    #draw background
    screen.blit(background, (0, 0))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()


        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())




    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    floorX -= 1
    draw_floor()
    if floorX <= -576:
        floorX= 0



    player(playerX,playerY)


    pygame.display.update()
pygame.quit()




