"""This is the class to create the actual cards"""

import pygame
from game import CardsData


class Board:

    """initiate class. The master class is the pygame instance we have already created"""
    def __init__(self, master):
        self.master = master
        self.properties = self.populate_board_cards()

    # Method to get the data from the CardsData class and create images of the cards for the board
    def populate_board_cards(self):
        data_dict = CardsData().return_dict_card_data()
        images_dictionary = dict()
        for key in data_dict.keys():
            rect_card = pygame.draw.rect(self.master, (0, 0, 0), pygame.Rect(30, 30, 60, 60))
            images_dictionary[key] = rect_card
        return images_dictionary

