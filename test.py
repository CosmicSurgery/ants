import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Filled Circular Sector")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set radius and angles
r = 100
theta_1 = 0  # Start angle in radians
theta_2 = math.pi / 2  # End angle in radians

# Set center of the circle
center = (width // 2, height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw filled circular sector
    pygame.draw.arc(screen, BLACK, (center[0] - r, center[1] - r, 2 * r, 2 * r), theta_1, theta_2, 0)
    pygame.draw.polygon(screen, BLACK, [center, (center[0] + r*math.cos(theta_1), center[1] - r*math.sin(theta_1)),
                                        (center[0] + r*math.cos(theta_2), center[1] - r*math.sin(theta_2))])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
