import pygame
import random

class Food:
    def __init__(self, x, y):
        self.position = (x, y)
        self.radius = 10
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.position, self.radius)