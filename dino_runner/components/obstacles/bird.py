from dino_runner.components.obstacles.obstacle import Obstacle
import random 
from dino_runner.utils.constants import LARGE_CACTUS


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice([310, 250, 220])





