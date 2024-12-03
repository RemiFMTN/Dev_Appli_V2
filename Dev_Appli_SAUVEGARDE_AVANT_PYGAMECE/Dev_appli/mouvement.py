import pygame

gravite = 0.40
reduction_grav = 0.4
boost = 2
force_saut = 35
player_speed = 6

# Variables de mouvement (vitesse)
move_x, move_y = 0, 0

def gestion_deplacement(event, move_x, move_y, player_speed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            move_x = player_speed
        if event.key == pygame.K_LEFT:
            move_x = -player_speed
        if event.key == pygame.K_SPACE:
            move_y = force_saut
        if event.key == pygame.K_LSHIFT:
            player_speed *= boost
    if event.type == pygame.KEYUP:
        if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
            move_x = 0
        if event.key == pygame.K_LSHIFT:
            player_speed /= boost

    return move_x, move_y, player_speed