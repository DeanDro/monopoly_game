# Class to capture the community cards

from cards_classes.cards import Cards


class Community(Cards):

    def __init__(self, card_name, saleable, message):
        super().__init__(self, card_name, saleable)
        self.message = message

    def return_card_message(self):
        """This is a function to return the message in the card
        """
        return self.message
