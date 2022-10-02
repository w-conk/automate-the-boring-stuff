import random

#variables
n_runs = 10000
flips_per_run = 100
total_instances = n_runs * flips_per_run
coinFlip = []
streak = 0
numberOfStreaks = 0

for experimentNumber in range(n_runs):
    # Code that creates a list of 100 'heads' or 'tails' values.'
    for i in range(flips_per_run):
        coinFlip.append(random.randint(0,1))
        if i==0:
            pass
        elif coinFlip[i] == coinFlip[i-1]:
            streak += 1
        else: 
            streak = 0

        if streak == 5:
            numberOfStreaks += 1

    coinFlip = []

#calculation for chance as a decimal    
chance = (numberOfStreaks / total_instances)
#function that converts decimal to percent and rounds
def to_percent(decimal):
    return round(decimal * 100,4)
#function call to convert result
chance_percent = to_percent(chance)
#print result 
print('Chance of streak: %s%%' % chance_percent)