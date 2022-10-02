import random

headsList = []
for i in range(100):
    headsList.append(random.randint(0,1))
print(headsList)
    #Code that checks if there is a streak of 6 heads or tails in a row
for i in range(len(headsList)):
    currentItem = headsList[i]
    if i == 0:
        previousItem = 0
    else:
        previousItem = headslist[i-1]
    
    sameCounter = 0
    if currentItem == previousItem:
        sameCounter += 1
    print(sameCounter)