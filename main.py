import pygame

from config import *
from particle import Particle
from image_loader import load_image_points

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/bg.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tirumala Particle Animation")

clock = pygame.time.Clock()

# Load image points
points = load_image_points(
    "assets/tirumala.png",
    WIDTH,
    HEIGHT,
    step=2
)

print("Image Points:", len(points))

# Create particles
particles = []

for i in range(len(points)):
    p = Particle(WIDTH, HEIGHT)
    x, y, color = points[i]
    p.set_target(x, y, color)
    particles.append(p)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for p in particles:
        p.move()
        p.draw(screen)

    pygame.display.flip()

pygame.quit()