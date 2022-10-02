#collatz sequence

def collatz(number):
        if number % 2 == 0:
            number = number // 2
            #print(number)
            return number
        elif number % 2 != 0:
            number = 3 * number + 1
            #print(number)
            return number

def collatzToOne(number):
    while True:
        if collatz(number) == 1:
            print('You made it to 1, bozo.')
            break
        else:
            number = collatz(number)
            print(number)

print('Enter Number')
try:
    number = int(input())
    collatzToOne(number)
except:
    print('You must enter an integer, moron.')


