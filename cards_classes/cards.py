"""Super class for all cards in the game"""

import pygame


class Cards:

    """Name, owner and saleable will be available across all cards"""
    def __init__(self, name, saleable, board_loc, owner=None):
        self.name = name
        self.board_loc = board_loc
        self.saleable = saleable
        self.owner = owner

    # Method to assign owner to a card if it is purchased
    def assign_owner(self, new_owner):
        self.owner = new_owner

    # Check who is the property owner
    def check_ownership(self):
        return self.owner

    def return_name(self):
        """In order for this method to return the name value for all children classes, each child class must
        have a global variable named self.name
        """
        return self.name
