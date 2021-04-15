# Method to capture the chance cards

from cards_classes.cards import Cards


class Chance(Cards):

    def __init__(self, card_name, saleable, board_loc, message):
        super().__init__(self, card_name, saleable, board_loc)
        self.message = message

    def return_chance_message(self):
        """Method to return the card message
        """
        return self.message
