"""Load the data from the excel file and convert them to json for the program to create
the cards"""

import pandas
from cards_classes.property import Properties


class CardsData:

    """initiate"""
    def __init__(self):
        self.excel_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='European Cities')
        self.cards_dictionary = self.return_dict_card_data()

    # Function to get the data loaded from excel to a dataframe and
    # then load the data from the dataframe to a dictionary of Properties class
    def return_dict_card_data(self):
        cards_dictionary = dict()
        city_names = self.excel_data['City']
        sell_value = self.excel_data['Sell Value']
        resell_value = self.excel_data['Resell Value']
        rent_value = self.excel_data['Rent']
        house_value = self.excel_data['house value']
        hotel_value = self.excel_data['hotel value']
        for i in range(0, 22):
            new_card = Properties(city_names[i], True, None, sell_value[i], rent_value[i],
                                  resell_value[i], house_value[i], hotel_value[i])
            cards_dictionary[city_names[i]] = new_card
        return cards_dictionary
