import pygame

class Player:
    def __init__(self, res_x):
        self.x = 0
        self.y = 0

        self.count = 0

        self.sprite = pygame.image.load("assets/sprite/idle.png")
        self.sprite = pygame.transform.scale(self.sprite, (round(res_x*0.03333), round(res_x*0.03333)))