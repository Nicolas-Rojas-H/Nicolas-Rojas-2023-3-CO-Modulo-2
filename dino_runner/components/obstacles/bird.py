from dino_runner.components.obstacles.obstacle import Obstacle
import random 
from dino_runner.utils.constants import LARGE_CACTUS
from pygame.sprite import Sprite

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice([310, 250, 210])
        self.index = 0

    def draw(self, screen):
     if self.index >= 9:
        self.index = 0

     screen.blit(self.image[self.index//5], self.rect)
     self.index += 1





