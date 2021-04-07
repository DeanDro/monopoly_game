"""Actual monopoly game"""

import pygame
import sys
import pandas
from cards_classes.property import Properties


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
        properties_data = CardsData().return_dict_card_data()
        horizontal = 1
        vertical = 1
        counter = 0
        for key in properties_data.keys():
            if counter < 11:
                point_x = horizontal * 50
                point_y = vertical * 30
                new_rect = pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 50, 70), 1)
                counter += 1
                horizontal +=1
            pygame.display.flip()


class CardsData:

    """initiate"""
    def __init__(self):
        self.excel_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='European Cities')
        self.cards_dictionary = self.return_dict_card_data()

    # Function to get the data loaded from excel to a dataframe and
    # then load the data from the dataframe to a dictionary of Properties class
    def return_dict_card_data(self):
        cards_dictionary = dict()
        city_names = self.excel_data['City']
        sell_value = self.excel_data['Sell Value']
        resell_value = self.excel_data['Resell Value']
        rent_value = self.excel_data['Rent']
        house_value = self.excel_data['house value']
        hotel_value = self.excel_data['hotel value']
        for i in range(0, 22):
            new_card = Properties(city_names[i], True, None, sell_value[i], rent_value[i],
                                  resell_value[i], house_value[i], hotel_value[i])
            cards_dictionary[city_names[i]] = new_card
        return cards_dictionary

