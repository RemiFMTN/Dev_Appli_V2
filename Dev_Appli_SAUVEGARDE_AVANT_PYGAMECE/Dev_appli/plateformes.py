import pygame
import random

Plateforme_min_longueur = 50
Plateforme_max_longueur = 200
Plateforme_largeur = 20
Plateforme_couleur = (0, 255, 255)

class Plateforme(pygame.Rect):
    def __init__ (self, x, y, longueur, largeur):
        super().__init__(x,y, longueur, largeur)

    def draw(self, ecran):
        pygame.draw.rect(ecran, Plateforme_couleur, self)

def generate_plateforms(num_plateformes, ecran_longueur, ecran_largeur):
    plateformes=[]
    for _ in range(num_plateformes):
        plateforme_longueur= random.randint(Plateforme_min_longueur, Plateforme_max_longueur)
        plateforme_x = random.randint(0, ecran_longueur - plateforme_longueur)
        plateforme_y = random.randint(50, ecran_largeur- Plateforme_largeur)
        plateforme = Plateforme(plateforme_x, plateforme_y, plateforme_longueur, Plateforme_largeur)
        plateformes.append(plateforme)
    return plateformes