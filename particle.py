import random
import pygame

class Particle:

    def __init__(self, width, height):

        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        self.tx = self.x
        self.ty = self.y

        self.speed = random.uniform(0.02, 0.08)
        self.angle = random.uniform(0, 6.28)
        self.radius = random.uniform(250, 500)
        self.timer = 180

    def set_target(self, x, y, color):
        self.tx = x
        self.ty = y
        self.color = color

    def move(self):

        import math

        if self.timer > 0:

            self.x = self.tx + math.cos(self.angle) * self.radius
            self.y = self.ty + math.sin(self.angle) * self.radius

            self.angle += 0.08
            self.radius *= 0.985
            self.timer -= 1

        else:

            dx = self.tx - self.x
            dy = self.ty - self.y

            self.x += dx * self.speed
            self.y += dy * self.speed

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            1
        )