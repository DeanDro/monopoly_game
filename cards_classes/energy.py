# Class to handle energy cards

from cards_classes.cards import Cards


class Energy(Cards):

    def __init__(self, card_name, saleable, board_loc, sell_value, resell_value, rent):
        super().__init__(self, card_name, saleable, board_loc)
        self.sell_value = sell_value
        self.resell_value = resell_value
        self.rent = rent

