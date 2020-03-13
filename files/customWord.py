#import
import random
import string
import charSet as cs

# read in word

customWord = "thisismytestword"
# customWord = input("Your word: ")

# functions

def randomize_case(letter):

    if letter == " ":
        letter = ""

    elif letter != " ":
        randomChoice = random.choice('abc')
        if randomChoice == 'a' :
            letter = letter.lower()
        elif randomChoice == 'b' :
            letter = letter.upper()
        elif randomChoice == 'c' :
            letter = letter

    return letter


def find_lookalike(letter):
    if letter.upper() in cs.specialsDict:
        letter = (random.choice(cs.specialsDict[letter.upper()]))
        return letter
    else:
        print('use only latin alphabet letters and no diacritic signs')
    return letter
    

# 1 - mix case randomly      
        
wordWithRandomCase = ''.join(randomize_case(letter) for letter in customWord)
print(wordWithRandomCase)

# 2 - letters to lookalike signs

weirdLookingWord = ''.join(find_lookalike(letter) for letter in customWord)
print(weirdLookingWord)

# 3 mix case randomly and change characters to special chars or numbers that are "lookalikes"
#   with two lookalikes

numberOfSpecialCharacters = 3
# numberOfSpecialCharacters = int(input("""
# How many letters in your word do you want to become
# special characters or special character clusters? 
# """))

def mix_chars_and_case(customWord):

    #create mixed case word to begin with
    wordWithRandomCase = ''.join(randomize_case(letter) for letter in customWord)

    # for the substitution operation, string to list conversion
    wordAsList = list(wordWithRandomCase)

    # choose the 'a' number of letters to be changed to specials
    # by getting their index number
    a = numberOfSpecialCharacters
    indexToChange = random.sample(range(len(customWord)), a)
    print(indexToChange)

    # get to all the chosen index numbers and change them to lookalike special characters
    for indexNumber in indexToChange:
        b = indexNumber
        letterToSubstitute = customWord[b]
        letterAsNewCharacter = find_lookalike(letterToSubstitute)
        wordAsList[b] = letterAsNewCharacter # substitution

    # list to string again
    mixedCaseAndSpecials = ''.join(wordAsList)
    return mixedCaseAndSpecials

print(mix_chars_and_case(customWord))

# 4 add special characters and/or numbers in between the word's letters
# OPTIONS: in the beginning, in the end, randomly within the word
# OPTIONS: add numbers, specialchars or both

numberOfNewSymbols = 2
chosenSet = cs.numbers

randomIndex = random.randint(0, len(customWord))

choice = 'end'
# for later use when choosing where to place chars:
if choice == 'end':
    position = 0
elif choice == 'beginning':
    position = len(customWord)
else:
    position = randomIndex

def add_new_symbols_randomly(customWord, position = randomIndex):

    a = numberOfNewSymbols
    wordAsList = list(customWord)

    for i in range(a):
        randomSymbol = random.choice(chosenSet)
        randomIndex = random.randint(0, len(customWord))
        wordAsList.insert(randomIndex, randomSymbol)
    
    return (''.join(wordAsList))

print(add_new_symbols_randomly(customWord))




def add_new_symbols_randomly(customWord):

    a = numberOfNewSymbols
    wordAsList = list(customWord)

    for i in range(a):
        randomSymbol = random.choice(chosenSet)
        randomIndex = random.randint(0, len(customWord))
        wordAsList.insert(randomIndex, randomSymbol)
    
    return (''.join(wordAsList))

# 6 and 7 can be built on the already existing functions