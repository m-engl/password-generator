# Read in user's word and:
# 1 mix case randomly
# 2 change characters to special chars or numbers that are "lookalikes"
# 3 or both of the above
# 4 add special characters and/or numbers in between the word's letters (SPECIFY LENGTH of the whole password)
# 5 mix case and add numbers
# 6 mix case and add special chars
# 7 mix case and add numbers and special characters

#import
import random
import string
import specialsDict as sd

# read in word

customWord = "thisismytestword"
# customWord = input("Your word: ")

# functions

def randomize_case(letter):

    randomChoice = random.choice('abc')

    if randomChoice == 'a' :
        letter = letter.lower()
    elif randomChoice == 'b' :
        letter = letter.upper()
    elif randomChoice == 'a' :
        letter = letter
    
    return letter


def find_lookalike(letter):
    if letter.upper() in sd.specialsDict:
        letter = (random.choice(sd.specialsDict[letter.upper()]))
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
        
    
    # 


print(mix_chars_and_case(customWord))