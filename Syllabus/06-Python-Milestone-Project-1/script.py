# Warm Up Project Exercises

"""
Write a program that checks if a user-input is within a range
"""


def user_choice():

    choice = 'Wrong'
    acceptable_range = range(0, 11)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number between 0 - 10: ')

        if choice.isdigit() == False:
            print('Sorry, that is an invalid choice.')

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print('That\'s correct!')
            else:
                within_range = False

    return int(choice)


user_choice()


"""
Milestone Project 1: Create a simple game program.
"""

game_list = [0, 1, 2]
play_values = ['0', '1', '2']
game_options = ['Y', 'N']


def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


display_game(game_list)


def position_choice():

    choice = 'wrong'

    while choice not in play_values:
        choice = input("Pick a position: 0,1 or 2: ")

        if choice not in play_values:
            print('That is not a valid choice.')

    return int(choice)


def replacement_choice(game_list, position):

    user_placement = input('Type a string to place at position: ')
    game_list[position] = user_placement

    print(game_list)


def game_on():

    choice = 'wrong'

    while choice not in game_options:
        choice = input("Keep playing: Y or N? ")

        if choice not in game_options:
            print('That is not a valid choice.')

    return int(choice)


position_choice()
replacement_choice(game_list, 1)
