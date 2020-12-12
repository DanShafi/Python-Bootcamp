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
