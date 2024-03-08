import pygame
from ant import Ant
from anthill import Anthill
from food import Food

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Ant Simulation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create objects
anthill = Anthill(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
ants = [Ant(anthill, i) for i in range(100)]  # Create 100 ants
food_sources = [Food(100, 100), Food(600, 400)]  # Create two food sources

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw objects
    anthill.draw(screen, RED)
    for ant in ants:
        ant.move()
        ant.draw(screen, BLACK)
    for food in food_sources:
        food.draw(screen, GREEN)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()