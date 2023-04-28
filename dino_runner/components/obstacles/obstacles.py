from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, JUMPING

class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT

    def update(self, game_speed):
        self.rect.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y)) 