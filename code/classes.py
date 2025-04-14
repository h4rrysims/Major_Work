import pygame
from os.path import join


class LiberalSprite(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'liberal.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.name = "Liberal"
        self.money = 1500 
    
    def move(self, new_pos):
        self.rect.center = new_pos
  
    def pay(self, amount):
        self.money -= amount
   
    def receive(self, amount):
        self.money += amount
    
class LabourSprite(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'Labour.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.name = "Labour"
        self.money = 1500 
   
    def move(self, new_pos):
        self.rect.center = new_pos
  
    def pay(self, amount):
        self.money -= amount
   
    def receive(self, amount):
        self.money += amount

class GreenSprite(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'Green.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.name = "Green"
        self.money = 1500 
   
    def move(self, new_pos):
        self.rect.center = new_pos
  
    def pay(self, amount):
        self.money -= amount
   
    def receive(self, amount):
        self.money += amount
