#coin flip streaks
import random

numberOfStreaks = 0
coinFlip = []
streak = 0

for experimentNumber in range(10000):
    #Code that creates a list of 100 heads or tails values
    for i in range(100):
        coinFlip.append(random.randint(0,1))
    #Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(coinFlip)):
        if i == 0:
            pass
        elif coinFlip[i] == coinFlip[i-1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 5:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))

        
        

