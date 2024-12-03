import pygame

import pygame

def init_musique(fichier: str, volume: float = 0.5):

    pygame.init()
    pygame.mixer.music.load(fichier)  # Charger la musique
    pygame.mixer.music.set_volume(volume)  # Régler le volume
    pygame.mixer.music.play(-1)  # Jouer en boucle
    print(f"Musique '{fichier}' jouée à un volume de {volume}. Appuyez sur Ctrl+C pour arrêter.")

def arreter_musique():

    pygame.mixer.music.stop()
    print("Musique arrêtée.")
