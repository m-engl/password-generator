import string

mainMenu = """
    === MAIN MENU ===
    Choose the option (enter number):
    1 - Generate a password
    2 - Generate customized password - use your custom word
    3 - Exit
    """

strengthChoiceMenu = """
        Choose the level/strength of your password:
                        1 - WEAK - lowercase and numbers
                        2 - MEDIUM - mixed case with numers
                        3 - STRONG - mixed case with numbers and special characters
                        Your choice: """

customPasswordMenu = """
    === CUSTOM PASSWORD MENU ===
    Before you enter the word you want to base your new password on,
    please choose the method of creating your password (enter number):
    1 - Mix case. 
        Example: 'word' --> wORd
    2 - Change all the letters in my word to special characters or numbers or sets thereof, that more or less look like these letters.
        Example: 'word' --> \/\/0|2|)
    3 - Choose how many letters should be changed to special characters. The rest is going to receive mixed case.
        Example: 1 special letter changed in the word 'word' --> wO|2d
    4 - Add a chosen number of special characters and/or numbers in between the word's letters.
        Example: 2 additional special characters randomly: 'word' --> $wo!rd
    5 - Mix case and add special characters or numbers or both
        Example: add numbers: 'word' -> Wo1rD
        """