import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1024,740))
pygame.display.set_caption('good mushrooms')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts\Alugu-Regular.ttf', 50)
game_active = True

sky_surface = pygame.image.load('assets\P9040042.JPG').convert()
sky_surface = pygame.transform.scale(sky_surface,(2048,1480))
sky_rect = sky_surface.get_rect(topleft = (0,0))
ground_surface = pygame.image.load('assets\P9040050.JPG').convert()
ground_surface = pygame.transform.scale(ground_surface,(12000,1480))
ground_rect = ground_surface.get_rect(topleft = (0,650))
test_surface = test_font.render('good mushrooms',False,'White')

game_message_surf = pygame.image.load('assets\game-over-1.png').convert()
game_message_rect = game_message_surf.get_rect(topleft = (0,0))

player_surf = pygame.image.load('assets\Asset 2.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (100,0))
player_gravity = 0
player_rect.y = 650


log_surf = pygame.image.load('assets\Rock-1.png').convert_alpha()
log_rect = log_surf.get_rect(bottomright = (1000,850))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                log_rect.x = 1000
                game_active = True
            if event.key == pygame.K_RIGHT:
                player_rect.x += 80
            if event.key == pygame.K_LEFT:
                player_rect.x -= 80
            if event.key == pygame.K_SPACE and player_rect.bottom >= 650:
                print('jump')
                player_gravity = -20
            if event.key == pygame.K_SPACE and game_active == False:
                log_rect.x = 1000
                game_active = True
            
    if game_active:
        #draw all of our elements
        #update everything
        screen.blit(sky_surface,sky_rect)
        sky_rect.x -= 1
        screen.blit(ground_surface,ground_rect)
        ground_rect.x -= 5.5
        ground_rect.x -= .2
        #screen.blit(test_surface,(300,200))
        
        #log movement
        screen.blit(log_surf,log_rect)
        log_rect.x -= 5.5
        log_rect.x -= .2
        if log_rect.right <= 0: log_rect.left = 1024
        
        #player movement
        screen.blit(player_surf,player_rect)
        #player_rect.x += 2
        if player_rect.left >= 1024: player_rect.right = 0
        player_gravity += .6
        player_rect.y += player_gravity
        if player_rect.bottom >= 650: player_rect.bottom = 650
        #print(f"PLAYER: (player_rect)")
        
        #game collision
        if log_rect.colliderect(player_rect):
            game_active = False
        
        #handles collisions
        if player_rect.colliderect(log_rect):
            print('COLLISION')
            print('____________________________________')
            print('.................')
        
        #mouse collision
        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            print("mouse")
            
    else:
        screen.blit(game_message_surf,game_message_rect)
    
    pygame.display.update()
    clock.tick(60)