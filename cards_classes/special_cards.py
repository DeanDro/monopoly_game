# Class to capture all the special case cards

from cards_classes.cards import Cards


class SpecialCards(Cards):

    def __init__(self, card_name, saleable_card, money_get, money_pay, action):
        super().__init__(self, card_name, saleable_card)
        self.money_get = money_get
        self.money_pay = money_pay
        self.action = action
