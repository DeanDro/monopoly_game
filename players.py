"""Parent class for creating both human and AI players"""
from cards_classes.cards import Cards


class Players:

    """
    A class that represents every player in the game.
    """

    def __init__(self, username_given, character_given, human=False):
        """
        Initialize the class by passing for arguments user name and character
        """
        self._username = username_given
        self._character = character_given
        self._money = 200000
        self._free = True
        self._cards = dict()
        self._total_value = 200000
        self._human = human

    # Method to get players total value
    def get_total_value(self):
        """Returns players total value"""
        return self._total_value

    # Method to add value to the player
    def set_player_value(self, additional_value):
        self._total_value += additional_value

    def set_cash(self, new_money):
        """Method to set cash value for the user"""
        self._money = new_money

    # Set if the user is human or AI
    def set_human_status(self, status):
        self._human = status

    # Method to adjust a card in the players deck of cards
    def add_card_players_stuck(self, card_var, command_option=None):
        self._cards.update(card_var)

    def set_character(self, new_character):
        """
        Method to set the character value
        """
        self._character = new_character

    def get_player_name(self):
        """Return user name"""
        return self._username

    def get_character(self):
        """Returns players character"""
        return self._character

    def get_money(self):
        """Returns available cash"""
        return self._money

    def get_cards(self):
        """Returns the dictionary with game cards"""
        return self._cards
