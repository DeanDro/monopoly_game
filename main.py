# Author: Konstantinos Drosos
# Date: 03/25/2021
# Description: This is a short version of a monopoly game to practice pygame and tkinter

import tkinter as tk
from tkinter import StringVar
"""
# Setup start window
root = tk.Tk()
root.geometry('400x400')
root.title('Crazy Monopoly')
root.configure(background='black')

# Labels for selections
title_label = tk.Label(root, text='Crazy Monopoly', font=('Arial', 25), background='black')
title_label.configure(fg='#f5f7f6')
title_label.grid(columnspan=3, row=0)

username_label = tk.Label(root, text='Username:', font=('Arial', 15), background='black')
username_label.configure(fg='#f5f7f6')
username_label.grid(column=0, row=1)

username_input = tk.Entry()
username_input.grid(column=1, row=1)

character_label = tk.Label(root, text='Select your character', font=('Arial', 15), background='black')
character_label.configure(fg='#f5f7f6')
character_label.grid(column=0, row=2, pady=20, padx=20)

available_characters = ['Car', 'Airplane', 'Boat', 'Rocket']
selected_character = StringVar()
selected_character.set('Car')
characters_dropdown = tk.OptionMenu(root, selected_character, *available_characters)
characters_dropdown.configure(fg='#f5f7f6', background='black')
characters_dropdown.grid(column=1, row=2, pady=20, padx=20)

number_opponents_label = tk.Label(root, text='Number of opponents', font=('Arial', 15), background='black')
number_opponents_label.configure(fg='#f5f7f6')
number_opponents_label.grid(column=0, row=3)

number_opponents = ['1', '2', '3']
num_opponents_selected = StringVar()
num_opponents_selected.set('1')
number_opponents_dropdown = tk.OptionMenu(root, num_opponents_selected, *number_opponents)
number_opponents_dropdown.configure(fg='#f5f7f6', background='black')
number_opponents_dropdown.grid(column=1, row=3)

start_game_button = tk.Button(root, text='Start Game', font=('Arial', 15), background='grey')
start_game_button.grid(column=0, row=4, pady=100)

cancel_button = tk.Button(root, text='Cancel', font=('Arial', 15), background='grey')
cancel_button.grid(column=1, row=4, padx=40)
"""

class Crazy_Monopoly(tk.Frame):

    """Set an class for the application"""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_labels('Crazy Monopoly', 0, 0)

    # Function to create a label giving the text and placement
    def create_labels(self, label_text, column_loc, row_loc):
        character_label = tk.Label(self.master, text=label_text, font=('Arial', 15), background='black')
        character_label.configure(fg='#f5f7f6')
        character_label.grid(column=column_loc, row=row_loc)

    # Helper function to create input
    def create_input_text(self, column_loc, row_loc):
        input_box = tk.Entry()
        input_box.grid(column=column_loc, row=row_loc)

    # Method to create dropdown box
    def create_dropdown(self, options, column_loc, row_loc):
        selection = tk.StringVar()
        selection.set(options[0])
        dropdown = tk.OptionMenu(self.master, selection, *options)
        dropdown.configure(fg='#f5f7f6')
        dropdown.grid(column=column_loc, row=row_loc)

    # Method to add a button
    def create_button(self, command, text_but, column_loc, row_loc):
        button = tk.Button(self.master, text=text_but, font=('Arial', 15), background='grey')
        button.grid(column=column_loc, row=row_loc)


root = tk.Tk()
crazy_monopoly = Crazy_Monopoly(root)
crazy_monopoly.mainloop()
