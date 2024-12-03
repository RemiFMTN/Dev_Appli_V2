def check_collisions(player_rect, velocite_joueur_y, plateformes):
    sur_sol = False  # On commence par supposer que le joueur n'est pas sur une plateforme.

    for plateforme in plateformes:
        if player_rect.colliderect(plateforme):  # Vérifier si le joueur entre en collision avec la plateforme
            # **Collision par le bas** (Le joueur tombe sur la plateforme)
            if velocite_joueur_y > 0 and player_rect.bottom <= plateforme.top + velocite_joueur_y:
                player_rect.bottom = plateforme.top  # Le joueur est mis juste au-dessus de la plateforme
                velocite_joueur_y = 0  # Arrêter la chute (gravitée)
                sur_sol = True
            # **Collision par le haut** (Le joueur heurte la plateforme par le haut)
            elif velocite_joueur_y < 0 and player_rect.top >= plateforme.bottom + velocite_joueur_y:
                player_rect.top = plateforme.bottom  # Le joueur est repoussé sous la plateforme
                velocite_joueur_y = 0  # Arrêter la vitesse verticale (pas de rebond)
            # **Collision par les côtés** (le joueur touche la plateforme à gauche ou à droite)
            elif player_rect.colliderect(plateforme):
                if player_rect.left < plateforme.right and player_rect.right > plateforme.left:
                    if player_rect.left < plateforme.left:  # Si la collision est par la gauche
                        player_rect.left = plateforme.right  # Le joueur est repoussé à droite
                    elif player_rect.right > plateforme.right:  # Si la collision est par la droite
                        player_rect.right = plateforme.left  # Le joueur est repoussé à gauche
            break  # Arrêter la boucle après avoir trouvé la première collision

    return velocite_joueur_y, sur_sol
