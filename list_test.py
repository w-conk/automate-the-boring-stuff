#list test
catList = []

while True:
    print(f'Enter the name of cat {len(catList)+1} (Or enter nothing to stop)')
    catName = input()
    if catName == '':
        break
    catList = catList + [catName]
print('The cat names are:')
for catName in catList:
    print(f' {catName}')