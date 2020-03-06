#==================================================
#======================IMPORT======================
#==================================================

import string
import random
from enum import Enum
from enum import IntEnum
import menus
import charSet as cs
import customWord as cw

#==================================================
#=====================CHOICES======================
#==================================================

MainMenu = IntEnum('MainMenu', {'GeneratePassword' : 1,
'CustomWord' : 2,
'Exit' : 3})

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

    startChoice = int(input(menus.mainMenu + "Your choice: " ))

############################################################

    if startChoice == MainMenu.Exit:
        print('\n *** EXIT ***\n')
        break

############################################################

    elif startChoice == MainMenu.GeneratePassword:
        
        print("\n" + "=== GENERATE PASSWORD ===" + "\n")

        length = int(input("""
        How long should the password be? 
                    Numer of characters: """))
        print("\n")

        strengthChoice = int(input(menus.strengthChoiceMenu))
        

        if strengthChoice == Strength.Weak:
            chosenSet = cs.weakSet

        elif strengthChoice == Strength.Medium:
            chosenSet = cs.mediumSet

        elif strengthChoice == Strength.Strong:
            chosenSet = cs.strongSet

        password = ''.join(random.choice(chosenSet) for _ in range(length))

        print('\n Here it is:', password)

############################################################

    elif startChoice == MainMenu.CustomWord:
        print("\n" + "=== GENERATE PASSWORD USING YOUR WORD ===" + "\n")
        insideCustomWordChoice = int(input((menus.customPasswordMenu + "YOUR CHOICE: "))


    )