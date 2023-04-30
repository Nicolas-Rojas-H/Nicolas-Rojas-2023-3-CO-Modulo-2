import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
from dino_runner.components.obstacles.bird import Bird
import random
class Obstacle_manager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        
        select = random.randint(0,1)

        if select == 0:
         obstacle = Bird(BIRD)
        elif select == 1:
         cactus = random.randint(0, 1)
         if cactus == 0:
          obstacle = Cactus(LARGE_CACTUS)
         elif cactus == 1:
          obstacle = Cactus(SMALL_CACTUS)
          
        return obstacle
    
    def update(self, game):
        if len(self.obstacles) == 0:
           obstacle = self.generate_obstacle()
           self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
           obstacle.update(game.game_speed, self.obstacles)
           if game.player.dino_rect.colliderect(obstacle.rect):
              pygame.time.delay(1000)
              game.playing = False
              break

    def draw(self, screen):
     for obstacle in self.obstacles:
      obstacle.draw(screen)