#pig latin

print('Enter the English message to translate into Pig Latin:')

phrase = input()
vowels = ('a','e','i','o','u','y')
pigLatin = []


for word in phrase.split():
    #separate the non-letters at the start of the word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    #separate the non-letters at the end of the word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[0:-1]
    #remember if the word was in uppercase or camel case:
    wasUpper = word.isupper()
    wasCamel = word.istitle()
    word = word.lower() #make the word lower case for translation
    #separate consanants at the start of the word
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants += word[0]
        word = word[1:]
    #add pig latin ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    #set the word back to title or uppercase
    if wasUpper:
        word = word.upper()
    if wasCamel:
        word = word.title()
    #add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin))


'''
for i in range(len(words)):
    if words[i][0] in vowels:
        words[i] = words[i] + 'yay'
    else:
        words[i] = words[i][1:]+words[i][0]+'ay'

words = ' '.join(words)'''