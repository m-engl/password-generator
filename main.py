#==================================================
#======================IMPORT======================
#==================================================

import string
import random
from enum import Enum
from enum import IntEnum
import charSet as cs

# For later version: test to include custom word.
# User types in custom word(s). Change to input when used.
customWord = 'myTestWord'

#==================================================
#=====================CHOICES======================
#==================================================

MainMenu = IntEnum('MainMenu', {'GeneratePassword' : 1, 'Exit' : 2})

Strength = IntEnum(
            'Strength', 
            {'Weak' : 1, 'Medium' : 2, 'Strong' : 3} 
            )

#==================================================
#=======================MAIN=======================
#==================================================
 
print(
"""
Welcome to the password generator.
You are going to be asked for the length of your password
as well as for what kind of characters you want to use.
""")

#==================MAIN LOOP=======================

while(True):

    startChoice = int(input(
    """
    === MAIN MENU ===
    Choose the option (enter number):
    1 - Generate a password
    2 - Exit
    Your choice: """))

    if startChoice == MainMenu.Exit:
        print('\n *** EXIT ***\n')
        break

    elif startChoice == MainMenu.GeneratePassword:
        
        print("\n" + "=== GENERATE PASSWORD ===" + "\n")

        length = int(input("""
        How long should the password be? 
                    Numer of characters: """))
        print("\n")



        strengthChoice = int(input('''
        Choose the level/strength of your password:
                        1 - WEAK - lowercase and numbers
                        2 - MEDIUM - mixed case with numers
                        3 - STRONG - mixed case with numbers and special characters
                        Your choice: '''))
        

        if strengthChoice == Strength.Weak:
            chosenSet = cs.weakSet

        elif strengthChoice == Strength.Medium:
            chosenSet = cs.mediumSet

        elif strengthChoice == Strength.Strong:
            chosenSet = cs.strongSet

        password = ''.join(random.choice(chosenSet) for _ in range(length))

        print('\n Here it is:', password)

