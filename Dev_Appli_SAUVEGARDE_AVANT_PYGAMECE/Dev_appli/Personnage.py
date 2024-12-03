import pygame
import random

longueur_ecran = 1280
hauteur_ecran = 720
RED = (255, 0, 0)

move_x, move_y = 0, 0

# Definition de la classe joueur
class Player:
    def __init__(self, longueur, largeur):
        self.rect = pygame.Rect(0, 0, longueur, largeur)
    def show(self, FENETRE):
        pygame.draw.rect(FENETRE, (255,255,255), self.rect)
    def move(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y

# Création du joueur
def creer_joueur():
    return Player(20,20)

# Definition ennemi
class Ennemi:
    def __init__(self, x, y, hauteur, largeur, vitesse):
        self.x = x
        self.y = y
        self.hauteur = hauteur
        self.largeur = largeur
        self.vitesse = vitesse
        self.color = RED
    def dessiner(self, FENETRE):
        pygame.draw.rect(FENETRE, self.color, (self.x, self.y, self.largeur, self.hauteur))
    def mise_a_jour(self):
        self.x -= self.vitesse
        if self.x < -self.largeur:  # Réinitialiser si l'ennemi sort à gauche
            self.x = longueur_ecran
            self.y = random.randint(0, hauteur_ecran - self.hauteur)

# Création d'une liste d'ennemis
def creer_ennemis(nb_ennemis):
    ennemis = []
    for _ in range(nb_ennemis):
        x = random.randint(longueur_ecran, longueur_ecran + 200)
        y = random.randint(0, hauteur_ecran - 50)
        width = 50
        height = 50
        speed = random.randint(2, 5)
        ennemis.append(Ennemi(x, y, width, height, speed))
    return ennemis