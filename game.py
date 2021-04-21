"""Actual monopoly game"""
import random

import pygame
import sys
import pandas
from cards_classes.property import Properties
from cards_classes.special_cards import SpecialCards
from cards_classes.chance import Chance
from cards_classes.community import Community
from cards_classes.energy import Energy
from cards_classes.transportation import Transportation
from subplayers_classes.load_players import LoadPlayers


class Game:

    def __init__(self, username, num_opponents, user_character):
        pygame.init()
        self._username = username
        self._character = user_character
        self._number_opponents = int(num_opponents)
        self.screen = pygame.display.set_mode((1360, 700))
        self.running = True
        self.default_font = pygame.font.get_default_font()
        self.create_cards_on_board()
        # players name and information are loaded in the LoadPlayers class and there we generate the images
        # to be display on the regular screen.
        self.player = LoadPlayers(self.screen, self._username, 200000, 200000, self._number_opponents)
        self.player.return_images_on_screen()
        self.player.create_ai_opponents()
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
        properties_data = CardsData().return_complete_dictionary()
        # The horizontal will be increasing each time we add a card horizontally and the vertical each time we add a
        # card vertically
        horizontal = 1
        vertical = 1
        # When we stored the data, we set the board to start from location 0
        for i in range(0, 40):
            # in the Rect function point_x is the left point and point_y the top. The other two numbers is width
            # and height.
            if i < 11:
                point_x = horizontal * 70
                point_y = vertical * 50
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)

                # This is the helper method to paste the card names on the surface
                self.return_wrapped_card_name(properties_data, i, point_x, point_y, self.screen)
                # we are only increasing the horizontal counter because the blocks won't be going vertically down
                horizontal += 1
            elif 10 < i < 21:
                vertical += 1
                point_x = 11 * 70
                point_y = vertical * 50
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)
                self.return_wrapped_card_name(properties_data, i, point_x, point_y, self.screen)
            elif 20 < i < 31:
                # For the first time it enters in this loop we push the horizontal multiple 2 steps back because
                # in the last iteration of the first conditional, after it completed the last horizontal placement
                # it increased the horizontal value by 1.
                if i < 22:
                    horizontal -= 2
                # We have gone 10 times vertically down
                point_y = 11 * 50
                point_x = horizontal * 70
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)
                self.return_wrapped_card_name(properties_data, i, point_x, point_y, self.screen)
                # At this point we are decreasing the coordinate points going backwards to the board to close the loop
                horizontal -= 1
            else:
                vertical -= 1
                point_x = 70
                point_y = vertical * 50
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(point_x, point_y, 70, 50), 1)
                self.return_wrapped_card_name(properties_data, i, point_x, point_y, self.screen)
            pygame.display.flip()

    def return_wrapped_card_name(self, dictionary_with_data, dictionary_position, point_x, point_y, surface):
        """This method returns an image with the name of a card, wrapped to two lines if the name is longer than
        10 letters, so it can be pasted on the surface. It takes five arguments, the dictionary with the data,
        the position in the dictionary we want to extract data from, point_x and point_y which are the x and y
        coordinates for when we want the name to start appearing in the surface and the surface we want to paste
        the images on.
        """
        font_renderer = pygame.font.Font(self.default_font, 10)
        card = dictionary_with_data.get(dictionary_position).return_name()
        if len(card) > 10:
            str1 = ''
            str2 = ''
            counter = 0
            for character in str(card):
                if counter < 10:
                    str1 += character
                    counter += 1
                else:
                    str2 += character
                    counter += 1
            label1 = font_renderer.render(str1, 1, (255, 255, 255))
            label2 = font_renderer.render(str2, 1, (255, 255, 255))
            surface.blit(label1, (point_x + 5, point_y + 5))
            surface.blit(label2, (point_x + 5, point_y + 15))
        else:
            label = font_renderer.render(card, 1, (255, 255, 255))
            surface.blit(label, (point_x + 5, point_y + 5))


class CardsData:

    """initiate"""
    def __init__(self):
        self.cities_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='European Cities')
        self.special_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Special Cards')
        self.transportation_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Transportation')
        self.energy_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Energy')
        self.community_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Community Cards')
        self.chance_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='Chance Cards')
        self.complete_cards_dictionary = dict()
        self.populate_special_cards()
        self.populate_community_cards()
        self.populate_transportation()
        self.populate_chance_dict()
        self.populate_cities_dictionary()
        self.populate_energy_dict()

    def populate_cities_dictionary(self):
        """Helper method to populate complete_cards dictionary with the data from the dataframe.
        """
        city_names = self.cities_data['City']
        sell_value = self.cities_data['Sell Value']
        resell_value = self.cities_data['Resell Value']
        rent_value = self.cities_data['Rent']
        house_value = self.cities_data['house value']
        hotel_value = self.cities_data['hotel value']
        board_locations = self.cities_data['Board Location']
        for i in range(0, len(self.cities_data.index)):
            self.complete_cards_dictionary[board_locations[i]] = Properties(city_names[i], True, board_locations[i],
                                                                            sell_value[i], rent_value[i],
                                                                            resell_value[i], house_value[i],
                                                                            hotel_value[i])

    def populate_special_cards(self):
        """Method to populate complete_dict with special type cards.
        """
        block_name = self.special_data['Block']
        money_get = self.special_data['Money Get']
        money_pay = self.special_data['Money Lost']
        action_card = self.special_data['Action']
        board_loc = self.special_data['Board Location']
        for i in range(0, len(self.special_data.index)):
            self.complete_cards_dictionary[board_loc[i]] = SpecialCards(block_name[i], False, board_loc[i],
                                                                        money_get[i], money_pay[i], action_card[i])

    def populate_transportation(self):
        """Method to populate complete_dict with transportation cards.
        """
        route = self.transportation_data['Route']
        sell_value = self.transportation_data['Sell Value']
        resell_value = self.transportation_data['Resell Value']
        rent = self.transportation_data['Rent']
        board_loc = self.transportation_data['Board Location']
        for i in range(0, len(self.transportation_data.index)):
            self.complete_cards_dictionary[board_loc[i]] = Transportation(route[i], True, board_loc, sell_value[i],
                                                                          resell_value[i], rent[i])

    def populate_energy_dict(self):
        """Method to populate complete dictionary with the energy cards.
        """
        station = self.energy_data['Station']
        sell_value = self.energy_data['Sell Value']
        resell_value = self.energy_data['Resell Value']
        rent = self.energy_data['Rent']
        # The board location starts counting from 0 for the cards.
        board_loc = self.energy_data['Board Location']
        for i in range(0, len(self.energy_data.index)):
            self.complete_cards_dictionary[board_loc[i]] = Energy(station[i], True, board_loc,
                                                                  sell_value[i], resell_value[i], rent[i])

    def populate_chance_dict(self):
        """Method to populate complete dictionary with all the chance cards.
        """
        card_name = self.chance_data['Card']
        message = self.chance_data['Message']
        # Because we only have 3 chance boxes but multiple chance cards, the program will choose randomly
        # 3 cards for the 3 boxes
        # Because the range starts in 0 and we count the blocks starting at 1, we have to always take one number
        # less for each board location
        board_loc = [2, 16, 27]
        for i in range(0, 3):
            card_num = random.randint(1, 10)
            new_card = Chance(card_name[1], True, int(board_loc[i]), message[1])
            self.complete_cards_dictionary[int(board_loc[i])] = new_card

    def populate_community_cards(self):
        """Method to populate community cards in the complete_card dictionary.
        """
        card_name = self.community_data['Card']
        message = self.community_data['Message']
        # Because the range starts in 0 and we count the blocks starting at 1, we have to always take one number
        # less for each board location
        board_loc = [13, 22, 37]
        for i in range(0, 3):
            # card_num = random.randint(1, 11)
            new_card = Community(card_name[1], True, board_loc[i], message[1])
            self.complete_cards_dictionary[board_loc[i]] = new_card

    def return_complete_dictionary(self):
        """Method to return the dictionary with all the cards data.
        """
        return self.complete_cards_dictionary
