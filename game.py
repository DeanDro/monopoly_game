"""Actual monopoly game"""

import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.running = False
                # self.event_handler(event)
            pygame.display.update()

    # Method to start running the game
    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

    # Event handler function to track user interaction
    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            #pygame.quit()
        pygame.display.update()
