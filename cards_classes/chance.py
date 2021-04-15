# Method to capture the chance cards

from cards_classes.cards import Cards


class Chance(Cards):

    def __init__(self, card_name, saleable, message):
        super().__init__(self, card_name, saleable)
        self.message = message

    def return_chance_message(self):
        """Method to return the card message
        """
        return self.message
