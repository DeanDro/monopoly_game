# Method to handle the transportation cards

from cards_classes.cards import Cards


class Transportation(Cards):

    def __init__(self, card_name, saleable, board_loc, sell_value, resell_value, rent):
        super().__init__(self, card_name, saleable, board_loc)
        self.name = card_name
        self.sell_value = sell_value
        self.resell_value = resell_value
        self.rent = rent

