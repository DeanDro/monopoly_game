"""Actual monopoly game"""

import pygame
import sys
from game_board.board import Board
from game_board.load_card_data import CardsData


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.create_cards_on_board()
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

    # Method to get the cards from the Board class and draw the cards on the board
    def create_cards_on_board(self):
        properties_data = CardsData()
        print(properties_data.return_dict_card_data())
