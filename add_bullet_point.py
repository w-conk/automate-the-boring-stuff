#bullet point adder program

import pyperclip

#text = pyperclip.paste()

text = '''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''

textItems = text.split('\n')

for i in range(len(textItems)):
    textItems[i] = '*' + textItems[i]

text = '\n'.join(textItems)

print(text)
pyperclip.copy(text)


