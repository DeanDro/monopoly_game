"""Actual monopoly game"""

import pygame
import sys
import pandas
from cards_classes.property import Properties


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
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
        # The horizontal will be increasing each time we add a card horizontally and the vertical each time we add a
        # card vertically
        horizontal = 1
        vertical = 1
        counter = 0
        # In this running test we only have 22 cards in properties, so the program won't build more than 22 blocks
        for key in properties_data.keys():
            # in the Rect function point_x is the left point and point_y the top. The other two numbers is width
            # and height.
            if counter < 11:
                point_x = horizontal * 70
                point_y = vertical * 50
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)
                counter += 1
                # we are only increasing the horizontal counter because the blocks won't be going vertically down
                horizontal += 1
            elif 10 < counter < 21:
                vertical += 1
                point_x = 11 * 70
                point_y = vertical * 50
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)
                counter += 1
                print('Point_y before:', point_y)
                print('Point_x:', point_x)
            elif 20 < counter < 31:
                print('last counter:', counter)
                # At this point we are decreasing the coordinate points going backwards to the board to close the loop
                horizontal -= 2
                # We have gone 10 times vertically down
                point_y = 11 * 50
                print('Point_y: ', point_y)
                point_x = horizontal * 70
                print('Point_x:', point_x)
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)
                counter += 1
                print('Counter: ', counter)
            else:
                break
            pygame.display.flip()


class CardsData:

    """initiate"""
    def __init__(self):
        self.cities_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='European Cities')
        self.special_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Special Cards')
        self.transportation_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Transportation')
        self.energy_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Energy')
        self.community_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Community Cards')
        self.chance_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Chance Cards')
        self.cards_dictionary = self.return_dict_card_data()

    def return_dict_card_data(self):
        # Function to get the data loaded from excel to five different dataframes and
        # then load the data from the dataframes to a dictionary of each card type and then to a major dictionary that
        # will hold dictionaries from each card type
        cities_dictionary = dict()
        special_dictionary = dict()
        transportation_dictionary = dict()
        city_names = self.cities_data['City']
        sell_value = self.cities_data['Sell Value']
        resell_value = self.cities_data['Resell Value']
        rent_value = self.cities_data['Rent']
        house_value = self.cities_data['house value']
        hotel_value = self.cities_data['hotel value']
        for i in range(0, len(self.cities_data.index)):
            new_card = Properties(city_names[i], True, None, sell_value[i], rent_value[i],
                                  resell_value[i], house_value[i], hotel_value[i])
            cities_dictionary[city_names[i]] = new_card
        # Stopping here because realized i need to build special subclasses for the rest of the special cards
        return cities_dictionary

