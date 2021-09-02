import pygame,sys,random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos+276, 450))

def create_pipe ():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700,random_pipe_pos-200))
    return bottom_pipe , top_pipe

def move_pipes(pipes):
    for pipe in pipes :
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes :
        if pipe.bottom >= 513 :
            screen.blit(pipe_surface,pipe)
        else :
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
#intilizing the game
pygame.init()

#settig the screen
screen = pygame.display.set_mode((276,513))
clock = pygame.time.Clock()

#game variable
gravity = 0.1
bird_movement = 0

#adding the background
bg_surface = pygame.image.load('bg.png').convert()

#adding the floor
floor_surface = pygame.image.load('base.png').convert()
floor_x_pos = 0 #postion of the floor

#adding the bird
bird_surface = pygame.image.load('bird.png')
bird_rect = bird_surface.get_rect(center = (50,225))

#adding the pipe
pipe_surface = pygame.image.load('pipe.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,300,200]

#game loop
while True :
    for event in pygame.event.get():
        #if player want to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #adding the bird movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5

        #
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())




    #image is alwys drawn or moving the image
    screen.blit(bg_surface,(0,0))

    #bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)

    #pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)
    #floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -276:
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(120)