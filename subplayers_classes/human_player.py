"""Class for human users"""

from players import Players


class HumanPlayer(Players):

    """
    Initiate the character player
    """

    def __init__(self, username, character_given, status):
        super().__init__(self, username, character_given)
        super().set_human_status(status)
