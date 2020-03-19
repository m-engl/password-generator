import random
import charSet as cs


class Word_Based_Password:

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

    def find_lookalike(self, letter):

        if letter.upper() in cs.specialsDict:
            letter = (random.choice(cs.specialsDict[letter.upper()]))
            return letter

        else:
            return('ERROR: Your word should only consist of letters.')

    def mix_chars_and_case(self, customWord, n):

        # Step 1: randomize case in the word
        wordWithRandomCase = ''.join(self.randomize_case(letter) for letter in customWord)

        # Step 2: convert the string to list
        wordAsList = list(wordWithRandomCase)

        # Step 3: choose an 'n' number of letters to be changed to specials
        # by getting their index number - randomly
        indexToChange = random.sample(range(0, len(customWord)), int(n))
        # print(indexToChange)

        # get to all the chosen index numbers and change them to lookalike special characters
        for indexNumber in indexToChange:
            x = indexNumber
            letterToSubstitute = customWord[x]
            letterAsNewCharacter = self.find_lookalike(letterToSubstitute)
            wordAsList[x] = letterAsNewCharacter  # substitution

        # convert the list to a string again
        mixedCaseAndSpecials = ''.join(wordAsList)
        return mixedCaseAndSpecials

    def add_new_characters(self, customWord, n, chosenSet):

        wordAsList = list(customWord)

        for i in range(int(n)):
            randomSymbol = random.choice(chosenSet)
            randomIndex = random.randint(0, len(customWord))
            wordAsList.insert(randomIndex, randomSymbol)
            i += 1

        return (''.join(wordAsList))

    def generate_word_based_password(self, theWord, choicesLevel1,
                                     numberMixChange=2, numberAddSigns=3,
                                     choicesLevel2=[1, 0, 0]):

        self.theWord = theWord # the word the user has entered
        self.choicesLevel1 = choicesLevel1 # choice from the radiobuttons - value 1, 2, 3 or 4
        self.numberMixChange = numberMixChange # under Radiobutton No. 3, "How many letters do you want
                                               # to have changed to specials or numbers?"
        self.choicesLevel2 = choicesLevel2 # choice from the checkboxes under radiobutton No.4
        self.numberAddSigns = numberAddSigns # under Radiobutton No. 4, "How many signs do you want to add?"

        self.randomized = ''.join(self.randomize_case(sign) for sign in self.theWord)

        if self.choicesLevel1 == 1: # Mix case randomly
            self.password = self.randomized

        elif self.choicesLevel1 == 2: # Change all the letters to look-alike\nnumbers and special characters
            self.password = "".join(self.find_lookalike(sign) for sign in self.theWord)

        elif self.choicesLevel1 == 3: # Mix case and change a chosen number of letters to special characters and/or numbers
            # self.wordWithRandomCase = "".join(self.find_lookalike(sign) for sign in self.theWord)
            self.password = self.mix_chars_and_case(self.theWord, self.numberMixChange)

        elif self.choicesLevel1 == 4: # Add a chosen number of special characters and/or numbers in between the word's letters
            if choicesLevel2 == [1, 0, 0]:  # NUMBERS:
                usersChoices = cs.numbers
                self.password = self.add_new_characters(self.theWord, self.numberAddSigns, usersChoices)

            elif choicesLevel2 == [0, 1, 0]:  # SPECIALS
                usersChoices = cs.specialChars
                self.password = self.add_new_characters(self.theWord, self.numberAddSigns, usersChoices)

            elif choicesLevel2 == [1, 1, 0]:  # NUMBERS AND/OR SPECIALS
                usersChoices = cs.specialChars + cs.numbers
                self.password = self.add_new_characters(self.theWord, self.numberAddSigns, usersChoices)

            elif choicesLevel2 == [1, 0, 1]:  # NUMBERS + MIXED CASE
                usersChoices = cs.numbers
                self.password =  self.add_new_characters(self.randomized, self.numberAddSigns, usersChoices)

            elif choicesLevel2 == [0, 1, 1]:  # SPECIALS + MIXED CASE
                usersChoices = cs.specialChars
                self.password =  self.add_new_characters(self.randomized, self.numberAddSigns, usersChoices)

            elif choicesLevel2 == [0, 0, 1]:  # MIXED CASE
                self.password = self.randomized

            elif choicesLevel2 == [1, 1, 1]:  # MIXED CASE, NUMBERS AND SPECIALS
                usersChoices = cs.specialChars + cs.numbers
                self.password =  self.add_new_characters(self.randomized, self.numberAddSigns, usersChoices)

            else:
                self.password = "PROMPT: Choose your options!"

        return self.password
