"""Computer players"""

from players import Players


class AIPlayer(Players):

    """initiate class and set human to false"""
    def __init__(self, status):
        super().__init__(self)
        super().set_human_status(status)

