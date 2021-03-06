import random
import charSet as cs


class Sequence_Based_Generator:

    def __init__(self):
        self.password = "PROMPT: Select options!"

    def randomize_case(self, letter):

        if letter == " ":
            letter = ""

        elif letter != " ":
            randomChoice = random.choice('abc')
            if randomChoice == 'a':
                letter = letter.lower()
            elif randomChoice == 'b':
                letter = letter.upper()
            elif randomChoice == 'c':
                letter = letter

        return letter

    def spaces_to_specials(self, sign):
        if sign == " ":
            sign = random.choice(cs.specialChars)
            return sign
        else:
            return sign

    def spaces_to_numbers(self, sign):
        if sign == " ":
            sign = random.choice(cs.numbers)
            return sign
        else:
            return sign

    def spaces_to_numbers_or_specials(self, sign):
        randomChoice = random.choice('abc')
        if sign == " ":
            if randomChoice == 'a' :
                sign = random.choice(cs.numbers)
                return sign
            elif randomChoice == 'b' :
                sign = random.choice(cs.specialChars)
                return sign
            elif randomChoice == 'c' :
                sign = random.choice(cs.numbers) + random.choice(cs.specialChars)
                return sign
        else:
            return sign

    def generate_sequence_based_password(self, sequence, choices):

        self.sequence = sequence
        self.choices = choices

        if choices == [1, 0, 0]: # NUMBERS
            self.password = ''.join(self.spaces_to_numbers(sign) for sign in self.sequence)

        elif choices == [1, 0, 1]: # NUMBERS + MIXED CASE
            self.numsAdded = ''.join(self.spaces_to_numbers(sign) for sign in self.sequence)
            self.password = ''.join(self.randomize_case(sign) for sign in self.numsAdded)

        elif choices == [0, 1, 0]: # SPECIALS
            self.password = ''.join(self.spaces_to_specials(sign) for sign in self.sequence)

        elif choices == [0, 1, 1]: # SPECIALS AND MIXED CASE
            self.specsAdded = ''.join(self.spaces_to_specials(sign) for sign in self.sequence)
            self.password = ''.join(self.randomize_case(sign) for sign in self.specsAdded)

        elif choices == [0, 0, 1]: # MIXED CASE
            self.password = ''.join(self.randomize_case(sign) for sign in self.sequence)

        elif choices == [1, 1, 0]: # NUMBERS AND/OR SPECIALS
            self.password = ''.join(self.spaces_to_numbers_or_specials(sign) for sign in self.sequence)

        elif choices == [1, 1, 1]: # MIXED CASE
            self.numsAndSpecsAdded = ''.join(self.spaces_to_numbers_or_specials(sign) for sign in self.sequence)
            self.password = ''.join(self.randomize_case(sign) for sign in self.numsAndSpecsAdded)

        else:
            self.password = "PROMPT: Choose your options!"

        return self.password



