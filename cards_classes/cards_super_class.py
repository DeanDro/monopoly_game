# All cards will be instances of this class

class CardsMegaClass:

    """
    The goal of CardsMegaClass is to create one class that all game cards will be children of.
    """

    def __init__(self, card_name, saleable, board_loc, owner=None, money_receive=None, money_pay=None,
                 action=None, card_cost=None, card_rent=None, resell_value=None, house_value=None,
                 hotel_value=None, message=None, card_type=None):
        """
        Instantiate the card with all arguments except name, board location and saleable set to None by default
        """
        self._card_name = card_name
        self._saleable = saleable
        self._board_loc = board_loc
        self._owner = owner
        self._money_receive = money_receive
        self._money_pay = money_pay
        self._action = action
        self._card_cost = card_cost
        self._card_rent = card_rent
        self._resell_value = resell_value
        self._house_value = house_value
        self._hotel_value = hotel_value
        self._message = message
        self._card_type = card_type

    def get_card_name(self):
        """
        Get the card name
        :return:
        """
        return self._card_name

    def get_saleable(self):
        """
        Returns if the card can be sold to a player
        :return:
        """
        return self._saleable

    def get_board_loc(self):
        """
        Returns the location of the card on the board
        :return:
        """
        return self._board_loc