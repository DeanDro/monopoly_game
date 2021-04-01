"""Parent class for creating both human and AI players"""


class Players:

    def __init__(self, username_given, character_given):
        self.username = username_given
        self.character = character_given
        self.money = 200000
        self.free = True
        self.cards = dict()
        self.total_value = 200000

    # Method to get players total value
    def get_player_value(self):
        return self.total_value

    # Method to add value to the player
    def set_player_value(self, additional_value):
        self.total_value += additional_value