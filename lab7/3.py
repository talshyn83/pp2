import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 500, 500
RADIUS = 25
STEP = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

x, y = WIDTH // 2, HEIGHT // 2
running = True

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIUS)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and y - RADIUS - STEP >= 0:
                y -= STEP
            elif event.key == K_DOWN and y + RADIUS + STEP <= HEIGHT:
                y += STEP
            elif event.key == K_LEFT and x - RADIUS - STEP >= 0:
                x -= STEP
            elif event.key == K_RIGHT and x + RADIUS + STEP <= WIDTH:
                x += STEP

pygame.quit()