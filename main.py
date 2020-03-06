#==================================================
#======================IMPORT======================
#==================================================

import string
import random
from enum import Enum
from enum import IntEnum

#==================================================
#==================CHARACTER SETS==================
#==================================================

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits
specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 

weakSet = lowerCase + numbers
mediumSet = lowerCase + upperCase + numbers
strongSet = lowerCase + upperCase + numbers + specialChars

# For later version: test to include custom word.
# User types in custom word(s). Change to input when used.
customWord = 'myTestWord'

#==================================================
#=======================MAIN=======================
#==================================================

print(
    """
Welcome to the password generator.
You are going to be asked for the length of your password
as well as for what kind of characters you want to use.
""")

length = int(input(
    """How long should the password be? 
                Numer of characters: """))

Strength = IntEnum(
    'Strength', 
    {'Weak' : 1, 'Medium' : 2, 'Strong' : 3} 
    )

strengthChoice = int(input('''
Choose the level/strength of your password:
                1 - WEAK - lowercase and numbers
                2 - MEDIUM - mixed case with numers
                3 - STRONG - mixed case with numbers and special characters
                Your choice: '''))

if strengthChoice == Strength.Weak:
    chosenSet = weakSet

elif strengthChoice == Strength.Medium:
    chosenSet = mediumSet

elif strengthChoice == Strength.Strong:
    chosenSet = strongSet

password = ''.join(random.choice(chosenSet) for _ in range(length))

print('Here it is:', password)

