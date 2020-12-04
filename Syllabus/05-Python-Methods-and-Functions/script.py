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

# Function Coding Exercises

""" Print Hello World """


def myfunc():
    print('Hello World')


""" Define a func that takes in a name arg """


def myfunc(name):
    print('Hello {}'.format(name))


""" Define a func that takes in a Bool and return an if statement """


def myfunc(x):
    if x == True:
        return 'Hello'
    else:
        return 'Goodbye'


""" Define a func that takes 3 args and return each other in an if logic """


def myfunc(x, y, z):
    if z == True:
        return x
    else:
        return y


""" Simple math """


def myfunc(x, y):
    return x + y


""" Return a bool if it's even/false """


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_greater(x, y):
    if x > y:
        return True
    else:
        return False


""" Def a func take that *args and returns a list containing only those args """


def myfunc(*args):
    result = []

    for num in args:
        if num % 2 == 0:
            result.append(num)

    return result


""" Def a func that upper() for each second index in a string """


def myfunc(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
