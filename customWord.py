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

# weirdLookingWord = ''.join(find_lookalike(letter) for letter in customWord)

print(random.choice(sd.specialsDict['w'.upper()]))
print(weirdLookingWord)