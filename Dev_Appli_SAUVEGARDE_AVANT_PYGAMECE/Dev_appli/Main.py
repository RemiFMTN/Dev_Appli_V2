import pygame
from plateformes import *
from Collisions import check_collisions
from Personnage import *
from mouvement import gestion_deplacement, gravite, reduction_grav, player_speed

# Initialisation Pygame
pygame.init()

# Musique de fond
pygame.mixer.music.load("Musique/Musique 1 pygame.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)  # Répéter indéfiniment

# Dimensions de la fenêtre
longueur_ecran = 1280
largeur_ecran = 720
FENETRE = pygame.display.set_mode((longueur_ecran, largeur_ecran))
pygame.display.set_caption("Le saut du Chevalier")

# Génération des plateformes
plateformes_genere = generate_plateforms(10, longueur_ecran, largeur_ecran)

#génération de la plateforme au sol
plateforme_sol = Plateforme(0, largeur_ecran - 20, longueur_ecran, 20)  # Plateforme au bas de l'écran
plateformes_genere.append(plateforme_sol)

# Création du joueur
cube = creer_joueur()

# Créer la liste des ennemis
liste_ennemis = creer_ennemis(5)

# Image de fond
fond = pygame.image.load("art-8396377_1920.png")
fond = pygame.transform.scale(fond, (longueur_ecran, largeur_ecran))

# Boucle principale
clock = pygame.time.Clock()
en_cours = True

while en_cours:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        # Gestion des déplacements
        move_x, move_y, player_speed = gestion_deplacement(event, move_x, move_y, player_speed)

        # Vérifier les collisions
        """velocite_joueur_y, sur_sol = check_collisions(cube.rect, velocite_joueur_y, plateformes_genere)"""

    # Application de la gravité
    move_y += gravite  # Gravité appliquée au joueur

    # Détection des bords de la fenêtre
    if cube.rect.x < 0:  # Bord gauche
        cube.rect.x = 0
    if cube.rect.x > longueur_ecran -20:  # Bord droit
        cube.rect.x = longueur_ecran - 20
    if cube.rect.y < 0:  # Plafond
        cube.rect.y = 0
    if cube.rect.y > largeur_ecran:  # Sol
        cube.rect.y = largeur_ecran
        move_y = -move_y * reduction_grav  # Inversion de la vitesse avec amortissement

        # Si la vitesse devient trop faible, arrêter le rebond
        if abs(move_y) < 0.5:
            move_y = 0

    """if not sur_sol:
        velocite_joueur_y += gravite
    move_y += velocite_joueur_y"""

    # Déplacer le joueur
    cube.move(move_x, move_y)

    # ----- Affichage ----- #

    # Dessiner l'image de fond
    FENETRE.blit(fond, (0, 0))
    # Afficher le joueur
    cube.show(FENETRE)

    # Affichage des ennemis
    for ennemi in liste_ennemis:
        ennemi.mise_a_jour()
        ennemi.dessiner(FENETRE)

    # Dessiner les plateformes
    for plateform in plateformes_genere:
        plateform.draw(FENETRE)

    pygame.display.update()

pygame.quit()
