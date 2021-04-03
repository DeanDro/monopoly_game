"""Class for human users"""

from players import Players


class HumanPlayer(Players):

    """Initiate the original method"""
    def __init__(self, status):
        super().__init__(self)
        super().set_human_status(status)
