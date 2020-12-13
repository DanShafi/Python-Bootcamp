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


def play_game():
    print('Would you like to play a game? Y or N? ')
    decision = input()
    decision.upper()

    if decision == 'y':
        print('Welcome to the game!')
        user_input()
    elif decision == 'n':
        print('Maybe next time!')
    else:
        print('That\'s not a valid selection.')


def user_input():
    print(f'This is the current list: {game_list}')
    user_choice = input('What position would you like to replace? 0, 1 or 2? ')

    if user_choice not in range(0, 3):
        print('That is an invalid selection.')
    else:
        game_changer()

    return int(user_choice)


play_game()
