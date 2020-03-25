# LEFT FRAME LOW


self.create_checkboxes_sequence(6) # arg: begin_with_row_number

def create_checkboxes_sequence(self, begin_with_row_number):
    self.i = begin_with_row_number
    for variableName, description in self.master.seqCHOICES:
        self.cb = tk.Checkbutton(self, text=description, variable=variableName)
        self.cb.grid(row=self.i, column=1, columnspan=4,
                     sticky='W')
        self.i += 1


# RIGHT

self.create_checkboxes_custom_word(14) # begin_with_row_number

def create_checkboxes_custom_word(self, begin_with_row_number):
        self.i = begin_with_row_number
        for variableName, description in self.master.addSpecialsCHOICES:
            variableName = tk.IntVar()
            self.cb = tk.Checkbutton(self, text=description,
                                     variable=variableName,
                                     anchor='w')
            self.cb.grid(row=self.i, column=0, columnspan=4,
                         padx=60,
                         sticky='W')
            self.i += 1

#GUI

 # PROGRAM METHODS
    # RANDOM PASSWORD GENERATING
    def get_length(self):
        self.length = self.leftFrameUpper.FieldEnterLength.get()
        self.leftFrameUpper.LabelUserEnteredLength.config(text = str(self.length))
        return self.length

    def get_strength(self):
        self.strength = self.ChooseStrength.get() # 1, 2, 3 or 4
        return self.strength

    def generate_random_password(self):
        length = int(self.get_length())
        strength = self.get_strength()
        self.chosenSet = cs.mediumSet

        if strength == 1:
            self.chosenSet = cs.weakSet
        elif strength == 2:
            self.chosenSet = cs.mediumSet
        elif strength == 3:
            self.chosenSet = cs.strongSet
        elif strength == 4:
            pass

        self.password = ''.join(random.choice(self.chosenSet) for _ in range(length))
        return self.password

    # SEQUENCE BASED-PWD GENERATING
    def get_sequence(self):
        self.sequence = self.leftFrameLower.FieldEnterSequence.get()
        self.leftFrameLower.LabelUserEnteredSequence.config(text = str(self.sequence))
        return self.sequence



    def generate_sequence_based_password(self):

        sequence = self.get_sequence()

        def spaces_to_specials(sign):
            if sign == " ":
                sign = random.choice(cs.specialChars)
                return sign
            else:
                return sign

        specialSequence = ''.join(spaces_to_specials(sign) for sign in sequence)  # cat]wants$food-badly
        specialSequenceMixed = ''.join(cw.randomize_case(sign) for sign in specialSequence)  # cat]wANTS$fOod-BadlY
        mixedSequence = ''.join(cw.randomize_case(sign) for sign in sequence)  # CAtwantsfOoDBAdlY

        self.password = specialSequence

    # WORD-BASED PWD

    def get_word(self):
        self.word = self.rightFrame.FieldEnterWord.get()
        self.rightFrame.LabelUserEnteredWord.config(text = str(self.word))
        return self.word


strengthMODES = [
    (1, "Weak"),
    (2, "Medium"),
    (3, "Strong"),
    (4, "Superstrong")
]

seqCHOICES = ["numbers", "special characters", "mixed case"]