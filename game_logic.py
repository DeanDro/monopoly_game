# This is a file to run the logic of the actual game
import random

import pygame
from players import Players


class MonopolyGameRules:

    def __init__(self, human_player, ai_player1, ai_player2=None):
        """Initialize the game and load all players"""
        self._human = human_player
        self._ai_player1 = ai_player1
        self._ai_player2 = ai_player2
        # we create a dictionary that holds the location of each player. We initialize everyone at the beginning
        self._players_positions = {'human': 0, 'ai_1': 0, 'ai_2': 0}
        # we always start with the human player
        self._players_turn = 1

    def roll_the_dice(self):
        """
        Moves the player 1 to 6 positions. It takes one argument, which players turn it is
        """
        dice = random.randint(1, 6)
        if self._players_turn == 1:
            current_pos = self._players_positions['human'] + dice
            box_pos = self.adjust_box_count(current_pos)
            self._players_positions['human'] = box_pos
            self._players_turn +=1
        elif self._players_turn == 2:
            current_pos = self._players_positions['ai_1'] + dice
            box_pos = self.adjust_box_count(current_pos)
            self._players_positions['ai_1'] = box_pos
            self._players_turn += 1
        else:
            if self._players_turn == 3 and self._ai_player2 is not None:
                current_pos = self._players_positions['ai_2'] + dice
                box_pos = self.adjust_box_count(current_pos)
                self._players_positions['ai_2'] = box_pos
                self._players_turn = 1
            else:
                self._players_turn = 1
                self.roll_the_dice()

    def check_card_status_and_decide(self, card):
        """AI player checks whether the card is owned by someone and decides to purchase or not."""
        if card.check_ownership == None:
            pass

    def load_players_positions(self, player_name, players_turn):
        """
        Method that takes the position of a player in terms of the number of the box and returns the coordinates of the
        player's character on the map. If the character passes starting point it get $200K in his account
        :return: The return value is a tuple with (x-coordinates, y-coordinates)
        """
        # x and y coordinates
        pos_x = 0
        pos_y = 0
        box_num = self._players_positions[player_name]
        if 0 <= box_num <= 10:
            pos_x = (11 - (11 - box_num)) * 70
            pos_y = 11 * 50
        elif 11 <= box_num <= 20:
            pos_x = 70
            pos_y = (11 - (11 - (box_num - 10))) * 50
        elif 21 <= box_num <= 30:
            pos_x = ((box_num - 20) + 1) * 70
            pos_y = 50
        elif 31 <= box_num <= 39:
            pos_x = 11 * 70
            pos_y = ((box_num - 30) + 1) * 50
        else:
            box_num -= 39
            # We setup the new position after it has gone through the starting point and we recursively call the
            # function again
            self._players_positions[player_name] = box_num
            players_turn.add_cash(200000)
            self.load_players_positions(player_name, players_turn)
        return pos_x, pos_y

    # Helper method to check if the position of the player has exceted the 39 count and return the box from the
    # beginning of the board
    def adjust_box_count(self, roll):
        if roll > 39:
            roll -= 39
        return roll

    # Method to get the position dictionary
    def get_players_position(self):
        return self._players_positions

    def confirm_number_players(self):
        if self._ai_player2 is None:
            return 2
        else:
            return 3

    def game_logic(self, cards_dictionary):
        """
        This function takes as a parameter the player currently playing and depending on whether it is a human or
        it is the ai gives option to human to purchase a card or make other actions or if it is AI decides how to
        proceed.
        :param player_currently:
        :return:
        """
        current_player = self._players_turn
        # We are looking at the total number of players
        number_players = self.confirm_number_players()
        if number_players == 2:
            if self._players_turn == 1:
                # Here we will put the methods to run the code for humans
                pass
            else:
                # The code for AI
                current_pos = self._players_positions['ai_1']
                # We have stored cards in the dictionary by the location
                current_card = cards_dictionary.get[current_pos]
                current_card_type = current_card.get_card_type()
                if current_card_type != 'Chance' or current_card_type != 'Community' or current_card_type != 'Special':
                    if current_card.get_owner() is None:
                        current_card.get_card_cost()
                        # we stop to the point where we get the cost of the new card
