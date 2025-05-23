import random

import pygame

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        # pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, divert):
        bisected = divert / 2
        change_direction = pygame.Vector2(
                self.velocity.x + bisected * 1.2,
                self.velocity.y + bisected * 1.2)
        return change_direction

    def split(self):
        self.kill()
        # Determine if if this shot asteroid needs to split or not.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Calculate new paths for slit asteroids
            divert = random.uniform(20, 50)
            new_vector1 = self.rotate(divert)
            new_vector2 = self.rotate(-divert)
            # Calculate size of new asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # Spawn new asteroids at collision point
            asteroid1 = Asteroid(
                    self.position.x,
                    self.position.y,
                    new_radius,
                    new_vector1)
            asteroid2 = Asteroid(
                    self.position.x,
                    self.position.y,
                    new_radius,
                    new_vector2)
