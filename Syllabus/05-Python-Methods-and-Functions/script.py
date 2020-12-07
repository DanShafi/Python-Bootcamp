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

# Function Practice Exercises


"""
Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
"""


def lesser_of_two_evens(x, y):
    if x and y % 2 == 0:
        if x < y:
            return x
        else:
            return y
    else:
        if x > y:
            result = x
        else:
            result = y

    return result


"""
Write a function that takes a two-word string and returns True if both words being with the same letter
"""


def animal_crackers(str):

    sp1, sp2 = str.split()

    if sp1[0] == sp1[0]:
        return True
    else:
        return False


"""
Write a function that when given two integers, return True if their sum is 20 or if one 
integer is 20. If not, return False
"""


def makes_twenty(n1, n2):
    return n1+n2 == 20 or n1 == 20 or n2 == 20

# Level One Problem Sets


"""
Write a function that capitalizes the first and fourth letters of a name
"""


def first_and_fourth(name):

    s = list(name)
    s[0] = s[0].upper()
    s[3] = s[3].upper()

    return "".join(s)


print(first_and_fourth('macdonald'))


"""
Write a function that takes in a string and reverses it's order like Yoda
"""


def master_yoda(phrase):

    li = list(phrase.split(" "))
    li.reverse()

    return ' '.join(li)


print(master_yoda('We Are Ready'))


# Level Two Problem Sets


"""
Given an integer n, write a function that returns True if n is within 10 of either
100 or 200.
"""


def almost_there(n):
    if n in range(90, 101) or n in range(190, 201):
        return True
    elif n in range(100, 111) or n in range(200, 211):
        return True
    else:
        return False


print(almost_there(205))
print(almost_there(89))
print(almost_there(56))
print(almost_there(93))
