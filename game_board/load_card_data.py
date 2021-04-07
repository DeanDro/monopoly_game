"""Load the data from the excel file and convert them to json for the program to create
the cards"""

import pandas
from cards_classes.property import Properties


class CardsData:

    """initiate"""
    def __init__(self):
        self.excel_data = pandas.read_excel('Monopoly_data.xlsx', sheet_name='European Cities')

    # Function to get the json data and return a dictionary of cards with all information
    def return_dict_card_data(self):
        city_names = self.excel_data['City']
        # sell_value = self.json_data.get('Sell Value')
        # resell_value = self.json_data.get('Resell Value')
        # rent_value = self.json_data.get('Rent')
        # house_value = self.json_data.get('house value')
        # hotel_value = self.json_data.get('hotel value')
        print(city_names)


test = CardsData()
test.return_dict_card_data()