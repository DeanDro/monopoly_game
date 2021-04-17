"""Computer players"""

from players import Players


class AIPlayer(Players):

    """initiate class and set human to false"""
    def __init__(self, username, character, status):
        super().__init__(self, username, character)
        super().set_human_status(status)

