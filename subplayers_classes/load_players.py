# Class to load the human player and the ai players in the game

from subplayers_classes.human_player import HumanPlayer
from subplayers_classes.ai_player import AIPlayer
import tkinter as tk


class LoadPlayers:

    """
    This is a method to create a canvas instance on the game window with information for the user player and the
    ai opponents.
    """

    def __init__(self, screen, human_player_name, human_total_value, **ai_details):
        """
        Instantiate a load players class and pass four arguments, the main screen where all information will be
        displayed, the human player username, the human total value and a dictionary with all information
        for the ai players.
        """
        self._screen = screen
        self.player_details = human_player_name
        self.human_total_value = human_total_value

    def return_images_on_screen(self):
        label_text = self.player_details + ': ' + self.human_total_value
        human_details = tk.Label(self._screen, text=label_text)
        return human_details
