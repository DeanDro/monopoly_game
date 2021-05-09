"""Actual monopoly game"""
import random

import pygame
import sys
import pandas
from subplayers_classes.load_players import LoadPlayers
from players import Players
from cards_classes.cards_super_class import CardsMegaClass
from game_logic import MonopolyGameRules


class Game:

    # A list of all possible characters in the game
    LIST_OF_CHARACTERS = ['Airplane', 'Boat', 'Boot', 'Car']
    CARDS_COLOR_PATTERNS = {1: (80, 70, 37), 3: (80, 70, 37), 6: (37, 82, 55), 8: (37, 82, 55), 9: (37, 82, 55),
                            11: (30, 29, 31), 13: (30, 29, 31), 14: (30, 29, 31), 16: (222, 4, 12), 18: (222, 4, 12),
                            19: (222, 4, 12), 21: (133, 118, 115), 23: (133, 118, 115), 24: (133, 118, 115),
                            26: (111, 21, 230), 27: (111, 21, 230), 29: (111, 21, 230), 31: (98, 189, 118),
                            32: (98, 189, 118), 34: (98, 189, 118), 37: (18, 17, 17), 39: (18, 17, 17)}

    def __init__(self, username, num_opponents, user_character):
        pygame.init()
        self._background_blue = (60, 25, 60)
        self._background_orange = (224, 81, 41)
        self._username = username
        self._character = user_character

        # We create placeholders for the images of the characters for the human and ai players. The actual loading
        # will happen later depending.
        self._human_character_img = None
        self._ai1_char_img = None
        self._ai2_char_img = None

        self._number_opponents = int(num_opponents)
        self.screen = pygame.display.set_mode((1360, 700))
        self.screen.fill(self._background_blue)
        self.running = True
        self.default_font = pygame.font.get_default_font()
        self.add_cards_color_pattern()
        self.create_cards_on_board()
        # Initialize the human player and the ai players dictionary and load them in the Monopoly Rules
        self._human_player = self.load_info_for_human()
        self._ai_dictionary = self.load_info_for_ai()
        self._game_rules = self.initiate_game_logic()
        self.update_players_position()
        # players name and information are loaded in the LoadPlayers class and there we generate the images
        # to be display on the regular screen.
        self.player = LoadPlayers(self.screen, self._human_player, self._ai_dictionary)
        self.player.return_images_on_screen()
        self.player.create_ai_opponents()

        # Control panel for the game
        self.roll_dice_button()
        # Players turn tracks whose player turn is. It updates each time after a player has made a move
        self._players_turns = 1

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
        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord = pygame.mouse.get_pos()
            if 990 < mouse_coord[0] < 1095 and 340 < mouse_coord[1] < 380:
                # In order to show movement on the board we have to redraw the board with all the information, but
                # with the position of the characters in their new coordinates.
                self._game_rules.roll_the_dice()
                self.screen.fill(self._background_blue)
                self.add_cards_color_pattern()
                self.create_cards_on_board()
                self.player.return_images_on_screen()
                self.player.create_ai_opponents()
                self.roll_dice_button()
                self.update_players_position()
                self._players_turns += 1

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
            label1 = font_renderer.render(str1, True, (255, 255, 255))
            label2 = font_renderer.render(str2, True, (255, 255, 255))
            surface.blit(label1, (point_x + 5, point_y + 5))
            surface.blit(label2, (point_x + 5, point_y + 15))
        else:
            label = font_renderer.render(card, True, (255, 255, 255))
            surface.blit(label, (point_x + 5, point_y + 5))

    def load_info_for_human(self):
        """this is a method to load username and all information for the human player"""
        human_player = Players(self._username, self._character, True)
        character_index = self.LIST_OF_CHARACTERS.index(self._character)
        character_name = str(self.LIST_OF_CHARACTERS.pop(character_index))+'.png'
        self._human_character_img = pygame.image.load(character_name)
        return human_player

    def load_info_for_ai(self):
        """This is a method to return a dictionary with all ai players"""
        ai_players = dict()
        for i in range(0, self._number_opponents):
            opponent_name = 'Player' + str(i+1)
            character_ai = self.LIST_OF_CHARACTERS.pop()
            ai_img = str(character_ai)+'.png'
            ai_ = Players(opponent_name, character_ai)
            if self._ai1_char_img is None:
                self._ai1_char_img = pygame.image.load(ai_img)
            else:
                self._ai2_char_img = pygame.image.load(ai_img)
            ai_players[i] = ai_
        return ai_players

    def roll_dice_button(self):
        """
        Method to create the button for rolling dice when player plays.
        """
        button_font = pygame.font.Font(pygame.font.get_default_font(), 20)
        roll_dice = button_font.render('Roll Dice', True, (255, 255, 255))
        pygame.draw.rect(self.screen, self._background_orange, (990, 340, 105, 40))
        pygame.display.update()
        self.screen.blit(roll_dice, (1000, 350))

    def initiate_game_logic(self):
        """
        This method looks at how many ai players are in the game and loads them in the game logic file along
        with the human player. This will also place the characters on the board for each player
        :return:
        """
        if self._number_opponents == 2:
            ai_1 = self._ai_dictionary.get('Player1')
            ai_2 = self._ai_dictionary.get('Player2')
            return MonopolyGameRules(self._human_player, ai_1, ai_2)
        else:
            return MonopolyGameRules(self._human_player, self._ai_dictionary.get('Player1'))

    # Method refreshes player character to be in the correct box after the dishes have been rolled
    def update_players_position(self):
        """
        This method blits the characters in the correct position after the roll position is executed.
        :return:
        """
        positions = self._game_rules.get_players_position()
        for key, value in positions.items():
            coord_x, coord_y = self.get_player_coordinates(value)
            if key == 'human':
                self.screen.blit(self._human_character_img, (coord_x, coord_y))
            elif key == 'ai_1':
                self.screen.blit(self._ai1_char_img, (coord_x, coord_y))
            else:
                pass
                # self.screen.blit(self._ai2_char_img, (coord_x, coord_y))

        # In the above we put the method that takes the current position and assigns the dimensions from the helper
        # method

    def get_player_coordinates(self, pos):
        """This is a helper method that takes the box # a player is in and returns the coordinates on the board"""
        if pos < 11:
            x = 770 - (pos * 70)
            y = 580
            return x, y
        elif 10 < pos < 21:
            coord = pos - 10
            x = 70
            y = 580 - (coord * 50)
            return x, y
        elif 20 < pos < 31:
            coord = pos - 20
            x = 70 + (70 * coord)
            y = 50
            return x, y
        else:
            coord = pos - 31
            x = 770
            y = 50 + (50 * coord)
            return x, y

    def add_cards_color_pattern(self):
        """This method rotates through the cards and adds a color pattern so you can create color groups"""
        for key, value in self.CARDS_COLOR_PATTERNS.items():
            coord = self.get_player_coordinates(key)
            pos_y = 0
            if key < 21:
                pos_y = coord[1] - 25
            elif 20 < key < 30:
                pos_y = coord[1]
            else:
                pos_y = coord[1] + 50
            color_box = pygame.draw.rect(self.screen, value, (coord[0], pos_y, 70, 25))
            pygame.display.update()


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
            self.complete_cards_dictionary[board_locations[i]] = CardsMegaClass(city_names[i], True, board_locations[i],
                                                                                card_cost=sell_value[i],
                                                                                card_rent=rent_value[i],
                                                                                resell_value=resell_value[i],
                                                                                house_value=house_value[i],
                                                                                hotel_value=hotel_value[i],
                                                                                card_type='Property')

    def populate_special_cards(self):
        """Method to populate complete_dict with special type cards.
        """
        block_name = self.special_data['Block']
        money_get = self.special_data['Money Get']
        money_pay = self.special_data['Money Lost']
        action_card = self.special_data['Action']
        board_loc = self.special_data['Board Location']
        for i in range(0, len(self.special_data.index)):
            self.complete_cards_dictionary[board_loc[i]] = CardsMegaClass(block_name[i], False, board_loc[i],
                                                                          money_receive=money_get[i],
                                                                          money_pay=money_pay[i],
                                                                          action=action_card[i],
                                                                          card_cost='Special')

    def populate_transportation(self):
        """Method to populate complete_dict with transportation cards.
        """
        route = self.transportation_data['Route']
        sell_value = self.transportation_data['Sell Value']
        resell_value = self.transportation_data['Resell Value']
        rent = self.transportation_data['Rent']
        board_loc = self.transportation_data['Board Location']
        for i in range(0, len(self.transportation_data.index)):
            self.complete_cards_dictionary[board_loc[i]] = CardsMegaClass(route[i], True, board_loc[i],
                                                                          card_cost=sell_value[i],
                                                                          resell_value=resell_value[i],
                                                                          card_rent=rent[i],
                                                                          card_type='Transportation')

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
            self.complete_cards_dictionary[board_loc[i]] = CardsMegaClass(station[i], True, board_loc[i],
                                                                          card_cost=sell_value[i],
                                                                          resell_value=resell_value[i],
                                                                          card_rent=rent[i],
                                                                          card_type='Energy')

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
            self.complete_cards_dictionary[int(board_loc[i])] = CardsMegaClass(card_name[i], False, int(board_loc[i]),
                                                                               message=message[1],
                                                                               card_type='Chance')

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
            self.complete_cards_dictionary[board_loc[i]] = CardsMegaClass(card_name[1], False, board_loc=board_loc[i],
                                                                          message=message[1], card_type='Community')

    def return_complete_dictionary(self):
        """Method to return the dictionary with all the cards data.
        """
        return self.complete_cards_dictionary
