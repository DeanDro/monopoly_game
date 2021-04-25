# This is a file to run the logic of the actual game
import random

import pygame
from players import Players


class MonopolyGameRules:

    def __init__(self, human_player, ai_player1, ai_player2=None, ai_player3=None):
        """Initialize the game and load all players"""
        self._human = human_player
        self._ai_player1 = ai_player1
        self._ai_player2 = ai_player2
        self._ai_player3 = ai_player3
        # we create a dictionary that holds the location of each player. We initialize everyone at the beginning
        self._players_positions = {'human': 0, 'ai_1': 0, 'ai_2': 0, 'ai_3': 0}

    def initiate_monopoly_game(self, turn_player):
        """
        Moves the player 1 to 6 positions. It takes one argument, which players turn it is
        """
        dice = random.randint(1, 6)
        if turn_player == 1:
            self._players_positions['human'] += dice
        elif turn_player == 2:
            self._players_positions['ai_1'] += dice
        elif turn_player == 3:
            self._players_positions['ai_2'] += dice
        else:
            self._players_positions['ai_3'] += dice

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
        if 0 <= box_num <=10:
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
        return (pos_x, pos_y)
