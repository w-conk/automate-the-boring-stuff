#code to play the game rock paper scissors

import random
import sys


wins = 0
losses = 0
ties = 0

while True: #main game loop
    print('ROCK, PAPER, SCISSORS')
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:
        print ('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break #break player input loop
        print('Type one of r, p, s, or q.')
    
    #display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    
    #display what computer chose
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
    
    #compute a win or not
    if computerMove == playerMove:
        ties += 1
        print('It is a tie!')
    elif (computerMove == 'p' and playerMove == 's') or (computerMove == 'r' and playerMove == 'p') or (computerMove == 's' and playerMove == 'r'):
        wins += 1
        print('You win!')
    elif (computerMove == 'p' and playerMove == 'r') or (computerMove == 'r' and playerMove == 's') or (computerMove == 's' and playerMove == 'p'):
        losses += 1
        print('You lose!') 