import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, JUMPING
from pygame.sprite import Sprite

class dinosaur(Sprite):
 X_POS = 80
 Y_POS = 310
 Y_DUCK = 345
 Jump_speed = 8.5
 def __init__(self):
     self.image = RUNNING[0]
     self.jump_speed = self.Jump_speed
     self.dino_rect = self.image.get_rect()
     self.dino_rect.x = self.X_POS
     self.dino_rect.y = self.Y_POS
     self.dino_run = True
     self.step_index = 0
     self.dino_jump = False
     self.dino_duck = False

 def update(self, user_input):
     if self.dino_run:
        self.run()
     elif self.dino_jump:
         self.jump()
     elif self.dino_duck:
         self.duck()

     if user_input[pygame.K_UP] and not self.dino_jump:
         self.dino_jump = True
         self.dino_run = False
     elif not self.dino_jump:
         self.dino_jump = False
         self.dino_run = True

     if user_input[pygame.K_DOWN]:
         self.dino_duck = True
         self.dino_run = False
     elif not self.dino_duck:
         self.dino_duck = False
         self.dino_run = True

     if self.step_index >= 10:
         self.step_index = 0
     

 def draw(self, screen):
      screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

 def run(self):
     self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
     self.dino_rect = self.image.get_rect()
     self.dino_rect.x = self.X_POS
     self.dino_rect.y = self.Y_POS
     self.step_index += 1

 def jump(self):
     self.image = JUMPING
     self.dino_rect.y -= self.jump_speed * 4
     self.jump_speed -= 0.8
     if self.jump_speed < -self.Jump_speed:
        self.dino_rect.y = self.Y_POS
        self.jump_speed = self.Jump_speed
        self.dino_jump = False

 def duck(self):
     
      self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
      self.dino_rect = self.image.get_rect()
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = self.Y_DUCK
      self.step_index += 1