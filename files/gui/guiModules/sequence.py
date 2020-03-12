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








def get_seq_choices(self):
    # print(self.leftFrameLower.numseq.get())
    pass

