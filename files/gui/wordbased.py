import random
import charSet as cs


class Word_Based_Password:

    def randomize_case(self, letter):

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

    def find_lookalike(self, letter):
        if letter.upper() in cs.specialsDict:
            letter = (random.choice(cs.specialsDict[letter.upper()]))
            return letter
        else:
            print('use only latin alphabet letters and no diacritic signs')
        return letter

    def generate_word_based_password(self, word, choicesLevel1, choicesLevel2=[0, 0, 0]):

        # word = self.word
        # choicesLevel1 = self.choicesLevel1
        # choicesLevel2 = self.choicesLevel2

        if choicesLevel1 == 1: # Mix case randomly
            self.password = ''.join(self.randomize_case(sign) for sign in word)

        elif choicesLevel1 == 2: # Change all the letters to look-alike\nnumbers and special characters
            print('2')

        elif choicesLevel1 == 3: # Mix case and change a chosen number of letters to special characters and/or numbers
            pass

        elif choicesLevel1 == 4: # Add a chosen number of special characters and/or numbers in between the word's letters
            pass



#######################################################

    # if choicesLevel2 == [1, 0, 0]:  # NUMBERS
    #     self.password = ''.join(self.spaces_to_numbers(sign) for sign in self.sequence)
    #
    # elif choicesLevel2 == [1, 0, 1]:  # NUMBERS + MIXED CASE
    #     self.numsAdded = ''.join(self.spaces_to_numbers(sign) for sign in self.sequence)
    #     self.password = ''.join(self.randomize_case(sign) for sign in self.numsAdded)
    #
    # elif choicesLevel2 == [0, 1, 0]:  # SPECIALS
    #     self.password = ''.join(self.spaces_to_specials(sign) for sign in self.sequence)
    #
    # elif choicesLevel2 == [0, 1, 1]:  # SPECIALS AND MIXED CASE
    #     self.specsAdded = ''.join(self.spaces_to_specials(sign) for sign in self.sequence)
    #     self.password = ''.join(self.randomize_case(sign) for sign in self.specsAdded)
    #
    # elif choicesLevel2 == [0, 0, 1]:  # MIXED CASE
    #     self.password = ''.join(self.randomize_case(sign) for sign in self.sequence)
    #
    # elif choicesLevel2 == [1, 1, 0]:  # NUMBERS AND/OR SPECIALS
    #     self.password = ''.join(self.spaces_to_numbers_or_specials(sign) for sign in self.sequence)
    #
    # elif choicesLevel2 == [1, 1, 1]:  # MIXED CASE, NUMBERS AND SPECIALS
    #     self.numsAndSpecsAdded = ''.join(self.spaces_to_numbers_or_specials(sign) for sign in self.sequence)
    #     self.password = ''.join(self.randomize_case(sign) for sign in self.numsAndSpecsAdded)
    #
    # else:
    #     self.message = "No option chosen!"

##############################################################

Wordy = Word_Based_Password()
print(Wordy.generate_word_based_password("blebleble", 2))
