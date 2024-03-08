import pygame

class Anthill:
    def __init__(self, x, y):
        self.position = (x, y)
        self.radius = 20

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.position, self.radius)