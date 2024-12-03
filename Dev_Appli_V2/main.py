from settings import *
from niveau import Niveau
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((LARGEUR_ECRAN, LONGUEUR_ECRAN))
        pygame.display.set_caption('Le saut du Chevalier')
        self.clock = pygame.time.Clock()

        self.tmx_maps = {0: load_pygame('data/niveaux/test.tmx')}
        self.current_map = Niveau(self.tmx_maps[0])

    def run(self):
        while True:
            dt = self.clock.tick(120) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_map.run(dt)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()