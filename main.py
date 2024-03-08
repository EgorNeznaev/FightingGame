import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1500, 600))
pygame.display.set_caption("Слово пацана")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


