import random
import math
import pygame
import numpy as np

class Ant:
    def __init__(self, anthill, unique_id):
        self.anthill = anthill
        self.unique_id = unique_id
        self.position = anthill.position
        self.direction = random.randint(0, 360)
        self.radius = 5
        self.has_food = False
        self.vision_radius = 50
        self.vision_angle = 120

    def move(self, food_sources, food_pheromone_matrix, home_pheromone_matrix):
        # Random wandering
        self.direction += random.randint(-30, 30)
        self.direction %= 360

        dx = math.cos(math.radians(self.direction)) * 2
        dy = math.sin(math.radians(self.direction)) * 2
        new_position = (self.position[0] + dx, self.position[1] + dy)

        # Function to check if a point is inside a circle
        def point_inside_circle(point, center, radius):
            x, y = point
            cx, cy = center
            distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            return distance <= radius

        # Check for food
        for food in food_sources:
            if np.linalg.norm(np.array(new_position) - np.array(food.position)) <= food.radius + self.radius:
                self.find_food(food_pheromone_matrix)
                break

        # Follow pheromone trails
        # pheromone_gradients = self.sense_pheromone(food_pheromone_matrix, home_pheromone_matrix)
        # if pheromone_gradients:
        #     resultant_gradient = np.sum(pheromone_gradients, axis=0)
        #     self.direction = math.degrees(math.atan2(resultant_gradient[1], resultant_gradient[0]))

        # Update position
        self.position = new_position
    
    def deposit_pheromone(self, pheromone_matrix, pheromone_type, intensity=1.0):
        pass
        # pheromone_matrix[int(self.position[1]), int(self.position[0])] += intensity

    # def sense_pheromone(self, food_pheromone_matrix, home_pheromone_matrix):
        # pheromone_gradients = []
        # for angle in range(-self.vision_angle // 2, self.vision_angle // 2 + 1):
        #     dx = math.cos(math.radians(self.direction + angle)) * self.vision_radius
        #     dy = math.sin(math.radians(self.direction + angle)) * self.vision_radius
        #     vision_position = (int(self.position[0] + dx), int(self.position[1] + dy))

        #     food_pheromone_intensity = food_pheromone_matrix[vision_position[1], vision_position[0]]
        #     home_pheromone_intensity = home_pheromone_matrix[vision_position[1], vision_position[0]]

        #     if food_pheromone_intensity > 0 or home_pheromone_intensity > 0:
        #         pheromone_gradient = np.array([dx, dy]) * (food_pheromone_intensity + home_pheromone_intensity)
        #         pheromone_gradients.append(pheromone_gradient)

        # return pheromone_gradients

    def find_food(self, food_pheromone_matrix):
        self.has_food = True
        self.deposit_pheromone(food_pheromone_matrix, "food", intensity=100.0)

    def return_to_anthill(self, home_pheromone_matrix):
        pass

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.position, self.radius)
        pygame.draw.circle(screen, color,self.position, self.radius)

    def __str__(self):
        return f"Ant {self.unique_id} at ({self.position})"