import random


def gameboard(board):

    game = ('\n'
            f' {board[0]} | {board[1]} | {board[2]} \n'
            f'-----------\n'
            f' {board[3]} | {board[4]} | {board[5]} \n'
            f'-----------\n'
            f' {board[6]} | {board[7]} | {board[8]} \n')
    return (game)


def turn(board, player, XorO):

    entry = (input(f'\n{player}: Where would you like to play?:'))

    try:
        entry = int(entry)
    except ValueError:
        print("\nInvalid input. Please try again.")
        return turn(board, player, XorO)

    if entry > 9 or entry < 1:
        print('\nInvalid input. Please try again.')
        return turn(board, player, XorO)
    elif board[entry - 1] in ('X', 'O'):
        print('\nSquare already filled. Please try again.')
        return turn(board, player, XorO)

    board[entry-1] = XorO
    print('\nAfter your turn:')
    print(gameboard(board))
    return board


def win_condition(board, XorO):
    winning_lines = [(0, 1, 2),
                     (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] == XorO:
            return True


def aiopponent(board, turn_count, illegal_move):
    if turn_count == 1:
        if board[4] != 'O':
            board[4] = 'X'
        else:
            board[random.choice([0, 2, 6, 8])] = 'X'
        return board

    ai_move = move_finder(board, illegal_move, 'X')

    if ai_move is None:
        ai_move = move_finder(board, illegal_move, 'O')

    if ai_move is None:
        ai_move = random.randint(0, len(board) - 1)
        while not isinstance(board[ai_move], int):
            ai_move = random.randint(0, len(board) - 1)

    board[ai_move] = 'X'

    return board


def move_finder(board, illegal_move, XorO):

    ai_move = None
    winning_lines = [(0, 1, 2),
                     (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_lines:
        if board[a] == board[b] == XorO and c not in illegal_move:
            ai_move = c
            break
        elif board[a] == board[c] == XorO and b not in illegal_move:
            ai_move = b
            break
        elif board[b] == board[c] == XorO and a not in illegal_move:
            ai_move = a
            break
    if ai_move == None:
        return None

    elif isinstance(board[ai_move], str):
        illegal_move.append(ai_move)
        return move_finder(board, illegal_move, XorO)

    return ai_move


def game():
    player1 = input('\nPlayer 1 enter your name:')
    player2 = input('\nPlayer 2 enter your name:')
    print('\nHere is the board:')

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(gameboard(board))

    turn_count = 0
    while turn_count < 9:
        board = turn(board, player1, 'O')
        if win_condition(board, 'O') == True:
            print(f'{player1} wins!')
            break

        turn_count += 1
        if turn_count == 9:
            print('It\'s a tie!')
            break

        board = turn(board, player2, 'X')
        if win_condition(board, 'X') == True:
            print(f'{player2} wins!')
            break
        turn_count += 1

    return print('\nGame Over!')


def aigame():
    illegal_move = []
    player = input('\nEnter your name: ')
    print('\nHere is the board:')
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(gameboard(board))

    turn_count = 0
    while turn_count < 9:
        board = turn(board, player, 'O')
        if win_condition(board, 'O') == True:
            print(f'{player} wins!')
            break

        turn_count += 1
        if turn_count == 9:
            print('It\'s a tie!')
            break

        board = aiopponent(board, turn_count, illegal_move)
        print('\nAfter the computer\'s turn:')
        print(gameboard(board))
        if win_condition(board, 'X') == True:
            print('Computer wins!')
            break
        turn_count += 1

    return print('\nGame Over!')


def main_menu():
    print("Welcome to Noughts and Crosses!\n")
    mode = input(
        'Would you like to play:\nMode 1: Single Player\nMode 2: Two Player\nEnter your choice: ')
    if mode == '2':
        print(game())
    elif mode == '1':
        print(aigame())
    else:
        print("\nTry again!\n")
        main_menu()


main_menu()

'''
ISSUES:

1. Computer will play a random move with potentially zero value if there is no immediate winning or losing move

'''
