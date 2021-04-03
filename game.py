"""Actual monopoly game"""

import pygame
import sys


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)
            pygame.display.update()

    # Event handler function to track user interaction
    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
            # We add the sys.exit() so when the player presses quit exit the program all together
            sys.exit()
