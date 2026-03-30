import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle_diff = random.uniform(20, 50)
        new_direction_1 = self.velocity.rotate(angle_diff)
        new_direction_2 = new_direction_1.rotate(-angle_diff)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = new_direction_1 * 1.2
        a2.velocity = new_direction_2 * 1.2
