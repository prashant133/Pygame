import pygame,sys,random
def play():
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

    def check_collision(pipes):
        for pipe in pipes:
             if bird_rect.colliderect(pipe):
                 death_sound.play()
                 return False
        if bird_rect.top <= -100 or bird_rect.bottom >= 450:
            death_sound.play()
            return False
        return True

    def rotate_bird(bird):
        new_bird = pygame.transform.rotozoom(bird,-bird_movement*3,1)
        return new_bird

    def score_display(game_state):
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True,(255,255,255))
            score_rect = score_surface.get_rect(center = (125,60))
            screen.blit(score_surface,score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(125, 60))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(125, 420))
            screen.blit(high_score_surface, high_score_rect)


    def update_score(score,high_score):
        if score > high_score:
            high_score = score
        return high_score

    #intilizing the sound
    pygame.mixer.pre_init(frequency=44100,channels=1,buffer=516)
    #intilizing the game
    pygame.init()

    #settig the screen
    screen = pygame.display.set_mode((276,513))
    clock = pygame.time.Clock()
    game_font = pygame.font.Font(pygame.font.get_default_font(),20)

    #game variable
    gravity = 0.1
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0

    #adding the background
    bg_surface = pygame.image.load('Image/bg.png').convert()

    #adding the floor
    floor_surface = pygame.image.load('Image/base.png').convert()
    floor_x_pos = 0 #postion of the floor

    #adding the bird
    bird_surface = pygame.image.load('Image/bird.png').convert_alpha()
    bird_rect = bird_surface.get_rect(center = (50,225))

    #adding the pipe
    pipe_surface = pygame.image.load('Image/pipe.png')
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,1200)
    pipe_height = [400,300,200]

    game_over_surface = pygame.image.load('Image/message.png').convert_alpha()
    game_over_rect  = game_over_surface.get_rect(center = (138,256))

    flap_sound = pygame.mixer.Sound('sound/sound_sfx_wing.wav')
    death_sound = pygame.mixer.Sound('sound/sound_sfx_hit.wav')
    score_sound = pygame.mixer.Sound('sound/sound_sfx_point.wav')
    score_sound_countdown = 100
    #game loop
    while True :
        for event in pygame.event.get():
            #if player want to close the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #adding the bird movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 5
                    flap_sound.play()

                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (50,225)
                    bird_movement = 0
                    score = 0


            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())




        #image is alwys drawn or moving the image
        screen.blit(bg_surface,(0,0))
        if game_active :
            #bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird,bird_rect)
            game_active = check_collision(pipe_list)

            #pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            score += 0.01
            score_display('main_game')
            score_sound_countdown -= 1
            if score_sound_countdown <= 0 :
                score_sound.play()
                score_sound_countdown =100

        else :
            screen.blit(game_over_surface,game_over_rect)
            high_score = update_score(score,high_score)
            score_display('game_over')

        #floor
        #movement of the floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -276:
            floor_x_pos = 0


        pygame.display.update()
        clock.tick(120)
