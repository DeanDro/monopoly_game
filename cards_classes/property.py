"""This is for the cards that represent properties in the game"""

from cards_classes.cards import Cards
from tkinter import messagebox


class Properties(Cards):

    """Initiate the new property card"""
    def __init__(self, name, saleable, owner, value, rent, resell_value, house_value, hotel_value):
        super().__init__(self, name, saleable)
        super().assign_owner(owner)
        self.value = value
        self.rent = rent
        self.resell_value = resell_value
        self.house_value = house_value
        self.hotel_value = hotel_value

    # Method to check if a property belongs to someone and then assign it to an owner
    def purchase_card(self, new_owner):
        if super().check_ownership() is None:
            super().assign_owner(new_owner)
        else:
            # create pop up window to let the player know someone else owns the card.
            # Pending function to collect rent
            messagebox.showinfo('Property already sold', 'This property belongs to another player')
