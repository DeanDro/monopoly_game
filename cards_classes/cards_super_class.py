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

    def return_name(self):
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

    def get_owner(self):
        """
        Returns the owner of the class
        :return:
        """
        return self._owner

    def get_money_receive(self):
        """
        Returns if the player in this card can get money
        :return:
        """
        return self._money_receive

    def get_money_pay(self):
        """
        Returns if you have to pay money
        :return:
        """
        return self._money_pay

    def get_action(self):
        """
        Returns if the player has to take some action after this card
        :return:
        """
        return self._action

    def get_card_cost(self):
        """
        Returns the cost to buy the card
        :return:
        """
        return self._card_cost

    def get_card_rent(self):
        """
        Returns the value a player has to pay for falling in this card
        :return:
        """
        return self._card_rent

    def get_card_resell_value(self):
        """
        Returns the resell value of a card
        :return:
        """
        return self._resell_value

    def get_house_value(self):
        """
        Returns the value to put a house in this card
        :return:
        """
        return self._house_value

    def get_hotel_value(self):
        """
        Returns the value to build a hotel on this card
        :return:
        """
        return self._hotel_value

    def get_message(self):
        """
        Returns the message that a card might hold
        :return:
        """
        return self._message

    def get_card_type(self):
        """
        Returns the type of the card. For example if it is a property card, energy, special, etc.
        :return:
        """
        return self._card_type

    def set_card_owner(self, new_owner):
        """
        Sets the new owner for a card that purchase it. It takes one argument, the player who bought the card.
        :param new_owner:
        :return:
        """
        self._owner = new_owner
