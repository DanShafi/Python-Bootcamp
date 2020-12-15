"""
Tic-Tac-Toe Game
"""

import random

game_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

"""
Display board to user.
"""


def display_board(board):

    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])


"""
Check to see what marker the players will have
"""


def player_input():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


"""
Takes in board list object, marker and assigns it to the board
"""


def place_marker(board, marker, position):
    board[position] = marker


"""
Take in board list and checks to see if the marker has won
"""

"""
Checking board to see if there is a winner
"""


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


"""
Picking the first player to make a move
"""


def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


"""
Check to see if the position on a board is free to place
"""


def space_check(board, position):
    return board[position] == ' '


"""
Check if board is full and return a boolean value
"""


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


"""
Ask player for next position as a number and use previous function to check if
that play can be made
"""


def player_choice(board):

    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position: 1-9: '))

    return position


"""
Write a function that asks the player if they want to play again
"""


def replay():

    choice = input('Play again? Enter Yes or No ')

    return choice == 'Yes'


"""
Logic
"""

print('Welcome to Tic Tac Toe')

while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will play first.')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won the game.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw.')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won the game.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw.')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        print('Thanks for playing Tic Tac Toe.')
        break
