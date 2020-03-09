import random
from enum import Enum
from enum import IntEnum
import charSet as cs

#==================================================
#=====================CHOICES======================
#==================================================

MainMenu = IntEnum(
    'MainMenu',
        {
        'GeneratePassword' : 1,
        'CustomWord' : 2,
        'Exit' : 3
        }
    )

Strength = IntEnum(
            'Strength',
            {'Weak' : 1, 'Medium' : 2, 'Strong' : 3}
            )

CustomWord = IntEnum(
    'CustomWord',
        {
        'MixCase' : 1,
        'Lookalikes' : 2,
        'MixedAndLookalikes' : 3,
        'AddSymbols' : 4,
        'MixedAndAddedSymbols' : 5
        }
)

class Random_Password:
    def __init__(self):
        self.length = 8
        self.chosenSet = cs.mediumSet
        self.strengthChoice = Strength.Medium
        self.password = "[null_password]"

    def ask_for_length(self):
        self.length = int(input("asking length:"))
        return self.length

    def ask_for_strength(self):

        self.strengthChoice = int(input("asking strength:"))

        if self.strengthChoice == Strength.Weak:
            self.chosenSet = cs.weakSet

        elif self.strengthChoice == Strength.Medium:
            self.chosenSet = cs.mediumSet

        elif self.strengthChoice == Strength.Strong:
            self.chosenSet = cs.strongSet

        return self.chosenSet

    def generate_password(self):
        self.password = ''.join(random.choice(self.chosenSet) for _ in range(self.length))
        return self.password









# TESTING
Pswrd = Random_Password()

Pswrd.ask_for_length()
Pswrd.ask_for_strength()
print(Pswrd.generate_password())
