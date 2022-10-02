#chapter 4 comma code
spam = ['apples','bananas','tofu','cats','turkey','bacon','naruto']


def comma_code(someParameter):
    stringToPrint = ''
    for i in range(len(someParameter)):
        if len(someParameter) == 0:
            stringToPrint = ''
        elif i == 0:
            stringToPrint = someParameter[i]
        elif i == len(someParameter)-1:
            stringToPrint = stringToPrint + ', and ' + someParameter[i]
        else:
            stringToPrint = stringToPrint + ', ' + someParameter[i]
    print(stringToPrint)


comma_code(spam)