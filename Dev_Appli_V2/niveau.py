from settings import *
from sprites import Sprite
from player import Player

class Niveau:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

        # Groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x, y, surf in  tmx_map.get_layer_by_name('test').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, self.collision_sprites)

        for obj in tmx_map.get_layer_by_name('Objets'):
            if obj.name == 'joueur':
                Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill('gray')
        self.all_sprites.draw(self.display_surface)