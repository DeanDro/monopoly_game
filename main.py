# Author: Konstantinos Drosos
# Date: 03/25/2021
# Description: This is a short version of a monopoly game to practice pygame and tkinter

import tkinter as tk
from tkinter import StringVar
from game import Game


class CrazyMonopoly(tk.Frame):

    """Set an class for the application"""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.username_value = tk.StringVar()
        self._number_players = tk.StringVar()
        self._player_character = tk.StringVar()
        self.create_labels('Crazy Monopoly', 0, 0, 2)
        self.create_labels('Username', 0, 1, 1, 15, 15)
        self.create_input_text(1, 1)
        self.create_labels('Select your character', 0, 2, 1, 15, 15)
        self.create_dropdown(['Car', 'Boat', 'Airplane', 'Boot'], 1, 2, self._player_character)
        self.create_labels('Number of opponents', 0, 3, 1, 15, 20)
        self.create_dropdown(['1', '2'], 1, 3, self._number_players)
        self.create_button('Start Game', 0, 4, self.start_game, 50)
        self.create_button('Cancel', 1, 4, self.close_game)

    # Function to create a label giving the text and placement
    def create_labels(self, label_text, column_loc, row_loc, column_length=None, x_gap=None, y_gap=None):
        character_label = tk.Label(self.master, text=label_text, font=('Arial', 15), bg='#3C193C')
        character_label.configure(fg='#f5f7f6')
        character_label.grid(column=column_loc, row=row_loc, columnspan=column_length,
                             padx=x_gap, pady=y_gap)

    # Helper function to create input
    def create_input_text(self, column_loc, row_loc):
        input_box = tk.Entry(self.master, textvariable = self.username_value, font=('calibre', 10, 'normal'))
        input_box.grid(column=column_loc, row=row_loc)

    # Method to create dropdown box
    def create_dropdown(self, options, column_loc, row_loc, variable):
        variable.set(options[0])
        dropdown = tk.OptionMenu(self.master, variable, *options)
        dropdown.configure(fg='#FFFFFF')
        dropdown.configure(bg='#3C193C')
        dropdown.grid(column=column_loc, row=row_loc)

    # Method to add a button
    def create_button(self, text_but, column_loc, row_loc, command_function=None, pad_y=None):
        button = tk.Button(self.master, text=text_but, font=('Arial', 15), bg='#D96A1E',
                           command=command_function)
        button.grid(column=column_loc, row=row_loc, pady=pad_y)

    # Method to close the window
    def close_game(self):
        self.master.quit()

    # Method to start the monopoly game
    def start_game(self) -> None:
        """
        We are calling the start game function and we pass the username value. For testing purposes we also pass that
        there will be 3 opponents and that users character is a boat.
        """
        username = self.username_value.get()
        number_of_opponents = self._number_players.get()
        player_character = self._player_character.get()
        self.start_game = Game(username, number_of_opponents, player_character)


root = tk.Tk()
root.geometry('400x400')
root.configure(bg='#3C193C')
root.title('Crazy Monopoly')
crazy_monopoly = CrazyMonopoly(root)
crazy_monopoly.mainloop()
