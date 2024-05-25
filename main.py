import pygame
import random

pygame.init()

#set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT)) 
pygame.display.set_caption("Dragon")


#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCLERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

#set colors
GREEN = (0 ,255, 0)
DARKGREEN = (10 , 50 , 10)
WHITE = (255 , 255 , 255)
BLACK = (0 , 0, 0)
WHITE = (255 ,255, 255)

#set fonts
font = pygame.font.Font('custom.ttf' , 32)
#set texts
score_text = font.render('Score' + str(score) , 1 , GREEN , DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10 , 10)

title_text = font.render('Feed the dragon' , 1 , GREEN , WHITE)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2 , 10)

lives_text = font.render("Lives: " + str(player_lives) , 1 , GREEN , DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10 , 10)

game_over_text = font.render("Game Over" , 1 , GREEN , DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to continue" , 1, GREEN , DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2 , WINDOW_HEIGHT // 2 + 35)
#set sounds and music
coin_sound = pygame.mixer.Sound('coin_sound.wav')
miss_sound = pygame.mixer.Sound('coin_miss.wav')
pygame.mixer.music.load('bg.wav')

#set images
dragon_img = pygame.image.load('dragon.png')
dragon_rect = dragon_img.get_rect()
dragon_rect.center = (55 , WINDOW_HEIGHT // 2)

coin_img = pygame.image.load('coin.png')
coin_rect = coin_img.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64 , WINDOW_HEIGHT - 40)

pygame.mixer.music.play(-1 , 0.0)
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_rect.top > 64:
        dragon_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += PLAYER_VELOCITY
    
    if coin_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64 , WINDOW_HEIGHT - 40)
    else:
        coin_rect.x -= coin_velocity
    
    if dragon_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCLERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64 , WINDOW_HEIGHT - 40)
    display_surface.fill(BLACK)

    display_surface.blit(score_text , score_rect)
    display_surface.blit(title_text , title_rect)
    display_surface.blit(lives_text , lives_rect)
    pygame.draw.line(display_surface , WHITE , (0, 64) , (WINDOW_WIDTH , 64))

    display_surface.blit(dragon_img , dragon_rect)
    display_surface.blit(coin_img , coin_rect)

    score_text = font.render('Score: ' +str(score) , 1 , GREEN , DARKGREEN)
    lives_text = font.render("Lives: " + str(player_lives) , 1 , GREEN , DARKGREEN)

    if player_lives == 0:
        display_surface.blit(game_over_text , game_over_rect)
        display_surface.blit(continue_text , continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    dragon_rect.y = WINDOW_HEIGHT //2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1 , 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()




