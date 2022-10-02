#rock paper scissors game

import random
import sys
print('ROCK, PAPER, SCISSORS')
print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')

wins = 0
losses = 0
ties = 0

while True:
    while True: #player input loop
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        elif playerMove =='r' or playerMove =='p' or playerMove =='s':
            break
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')

    #print player move
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    
    #print computer move
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    
    #compute
    if playerMove == computerMove:
        ties += 1
        print('It is a tie!')
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 'p' and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        wins += 1
        print('You win!')
    elif (playerMove == 'r' and computerMove == 'p') or (playerMove == 'p' and computerMove == 's') or (playerMove == 's' and computerMove == 'r'):
        losses += 1
        print('You lose!')
    
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')
