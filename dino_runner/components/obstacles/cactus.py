from dino_runner.components.obstacles.obstacle import Obstacle
import random 
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
class Cactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 330
        if image == LARGE_CACTUS:
            self.rect.y = 310
         
