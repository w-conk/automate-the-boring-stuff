#tic tac toe
import pprint
import sys

theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


while True:
    turn = 'X'
    print('Welcome to Tic-Tac-Toe!')
    print('Do you want to be X or O? (q)uit')
    while True: #player input loop to choose team
        playerTeam = input()
        if playerTeam == 'q':
            sys.exit()
        elif playerTeam =='X' or playerTeam =='O':
            break
        print('Please enter X or O.')
    while True:
        for i in range(9):
            printBoard(theBoard)
            print(f"Turn for {turn}. Move on which space? (top-, mid-, low-, L, M, R (eg. 'top-L')")
            move = input()
            if move not in theBoard.keys():
                print('Need a real space, pal.')
                break
            else:
                theBoard[move] =  turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
    printBoard(theBoard)       