# Read in user's word and:
# 1 mix case randomly
# 2 change characters to special chars or numbers that are "lookalikes"
# 3 or both of the above
# 4 add special characters and/or numbers in between the word's letters (SPECIFY LENGTH of the whole password)
# 5 mix case and add numbers
# 6 mix case and add special chars
# 7 mix case and add numbers and special characters

#import

import string
import random

# read in word

customWord = "thisIsATestWord"
# customWord = input("Your word: ")

# functions for case changing

def randomize_case(letter):

    randomChoice = random.choice('abc')

    if randomChoice == 'a' :
        letter = letter.lower()
    elif randomChoice == 'b' :
        letter = letter.upper()
    elif randomChoice == 'a' :
        letter = letter
    
    return letter

# 1 - mix case randomly      
        
wordWithRandomCase = ''.join(randomize_case(letter) for letter in customWord)

print(wordWithRandomCase)