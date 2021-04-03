"""Super class for all cards in the game"""

import pygame


class Cards:

    """Name, owner and saleable will be available across all cards"""
    def __init__(self, name, saleable, owner=None):
        self.name = name
        self.saleable = saleable
        self.owner = owner

    # Method to assign owner to a card if it is purchased
    def assign_owner(self, new_owner):
        self.owner = new_owner
