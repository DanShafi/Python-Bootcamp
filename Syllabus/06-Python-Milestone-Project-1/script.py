# Warm Up Project Exercises

"""
Write a program that checks if a user-input is within a range
"""


# def user_choice():

#     choice = 'Wrong'
#     acceptable_range = range(0, 11)
#     within_range = False

#     while choice.isdigit() == False or within_range == False:

#         choice = input('Please enter a number between 0 - 10: ')

#         if choice.isdigit() == False:
#             print('Sorry, that is an invalid choice.')

#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_range = True
#                 print('That\'s correct!')
#             else:
#                 within_range = False

#     return int(choice)


# user_choice()


"""
Milestone Project 1: Create a simple game program.
"""

game_list = [0, 1, 2]
play_values = ['0', '1', '2']
game_on = True


def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


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


def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep playing: Y or N? ")

        if choice not in ['Y', 'N']:
            print('Sorry. Please only choose Y or N.')

    if choice == 'Y':
        return True
    else:
        return False


while game_on:
    display_game(game_list)
    position = position_choice()
    replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()
    print('Thank you for playing! Goodbye.')
