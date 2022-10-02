#table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
'''
for i in range(len(tableData)):
    fullListLength = len(' '.join(tableData[i]))
    if fullListLength < len(' '.join(tableData[i+1])):
        fullListLength = ' '.join(tableData[i+1])
    print(' '.join(tableData[i]))
    print(fullListLength)
'''

for i in range(len(tableData)):
    print(len(' '.join(tableData[i])))


