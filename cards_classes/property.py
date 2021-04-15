"""This is for the cards that represent properties in the game"""

from cards_classes.cards import Cards
from tkinter import messagebox


class Properties(Cards):

    """Initiate the new property card"""
    def __init__(self, name, saleable, board_loc, value, rent, resell_value, house_value, hotel_value):
        super().__init__(self, name, saleable, board_loc)
        self.value = value
        self.rent = rent
        self.resell_value = resell_value
        self.house_value = house_value
        self.hotel_value = hotel_value

