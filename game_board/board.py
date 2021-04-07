"""This is the class to create the actual cards"""

import pygame
from cards_classes.property import Properties


class Board:

    """initiate class. The master class is the pygame instance we have already created"""
    def __init__(self, master):
        self.master = master
