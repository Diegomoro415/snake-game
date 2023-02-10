"""
import required libraries
"""
import pygame


# Initializes the display for the game".
pygame.display.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SnakeGame')

while True:
    for event in pygame.event.get():
        # pylint: disable=maybe-no-member
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
