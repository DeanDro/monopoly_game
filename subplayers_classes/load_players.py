# Class to load the human player and the ai players in the game
import pygame.font

from subplayers_classes.human_player import HumanPlayer
from subplayers_classes.ai_player import AIPlayer
import tkinter as tk


class LoadPlayers:

    """
    This is a method to create a canvas instance on the game window with information for the user player and the
    ai opponents.
    """

    def __init__(self, screen, human_player_name, human_total_value, human_player_cash, ai_details):
        """
        Instantiate a load players class and pass four arguments, the main screen where all information will be
        displayed, the human player username, the human total value and a dictionary with all information
        for the ai players.
        """
        self._screen = screen
        self._player_name = human_player_name
        self._human_total_value = human_total_value
        self._human_player_cash = human_player_cash
        self._ai_opponents = ai_details

    def return_images_on_screen(self):
        """This function creates a label with human players information and displays it on the page"""
        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, 15)
        pl_name = font.render(self._player_name, 1, (255, 255, 255))
        pl_cash = font.render('$'+str(self._human_player_cash), 1, (255, 255, 255))
        pl_total_value = font.render('$'+str(self._human_total_value), 1, (255, 255, 255))
        self._screen.blit(pl_name, (1000, 50))
        self._screen.blit(pl_cash, (1150, 50))
        self._screen.blit(pl_total_value, (1250, 50))

    def create_opponents_initial_values(self):
        """It creates a dictionary that includes all the information for the ai initial values"""

    def create_ai_opponents(self):
        """This method creates the image of opponents and attaches it to the dashboard"""
        starting_point = 2
        for ai in range(0, self._ai_opponents):
            loc_y = starting_point * 50
            ai_name = 'Player' + str(ai)
            font = pygame.font.Font(pygame.font.get_default_font(), 15)
            ai_player = font.render(ai_name, 1, (255, 255, 255))
            self._screen.blit(ai_player, (1000, loc_y))
            starting_point += 1
