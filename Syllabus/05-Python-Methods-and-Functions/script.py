from random import shuffle


def shuffle_list(mylist):
    """
    Takes the ball list and then shuffles it.
    """
    shuffle(mylist)
    return mylist


def player_guess():
    """
    Input function to ask the player to make
    a guess based on the index
    """
    guess = ''

    while guess not in [0, 1, 2]:
        guess = input('Pick a number: 0, 1 or 2? ')
        print('That is not a valid selection.')

    return int(guess)


def check_guess(mylist, guess):
    """
    Checks the player guess against the list index
    """
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)


mylist = [' ', 'O', ' ']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list, guess)
