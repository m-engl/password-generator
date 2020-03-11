import tkinter as tk
import random
from guiModules import UpperFrame as Upper_Frame
from guiModules import LeftFrameUP as Left_Frame_UP
from guiModules import LeftFrameLOW as Left_Frame_LOW
from guiModules import RightFrame as Right_Frame
from guiModules import LowerFrame as Lower_Frame
from chars import charSet as cs

root = tk.Tk()

# VARIABLES
theTitle = "My ULTIMATE (PASS)WORD Generator"
theLogo = "img/logo.gif"

strengthMODES = [
    (1, "Weak"),
    (2, "Medium"),
    (3, "Strong"),
    (4, "Superstrong")
]

seqCHOICES = ["numbers", "special characters", "mixed case"]

addSpecialsCHOICES = seqCHOICES

customWordMODES = [
    (1, "Mix case randomly"),
    (2, "Change all the letters to look-alike\nnumbers and special characters"),
    (3, "Mix case and change a chosen number \nof letters to special characters and/or numbers"),
    (4, "Add a chosen number of special characters and/or\nnumbers in between the word's letters")
]


# Here comes the main application class

class Main_Application(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title(theTitle)
        self.logo = tk.PhotoImage(file=theLogo)
        self.ChooseStrength = tk.IntVar()
        self.MainMenu = tk.IntVar()
        # Main Menu:
        # random password 1
        # word sequence based 2
        # custom word/crazy word based 3
        self.customWordChoice = tk.IntVar()
        self.strengthMODES = strengthMODES
        self.seqCHOICES = seqCHOICES
        self.addSpecialsCHOICES = addSpecialsCHOICES
        self.customWordMODES = customWordMODES
        self.length = tk.IntVar()
        self.strength = tk.IntVar()
        self.sequence = tk.StringVar()
        self.password = tk.StringVar()
        self.word = tk.StringVar()

        # FRAMES
        self.upperFrame = Upper_Frame.Upper_Frame(self, highlightbackground="black", highlightthickness=1)
        self.leftFrameUpper = Left_Frame_UP.Left_Frame_UP(self, highlightbackground="black", highlightthickness=1)  #
        self.leftFrameLower = Left_Frame_LOW.Left_Frame_LOW(self, highlightbackground="black", highlightthickness=1)  #
        self.rightFrame = Right_Frame.Right_Frame(self, highlightbackground="black", highlightthickness=1)  #
        self.lowerFrame = Lower_Frame.Lower_Frame(self, highlightbackground="black", highlightthickness=1)

        # LAYOUT
        self.upperFrame.grid(row=0, column=0, columnspan=2, sticky='NESW')
        self.leftFrameUpper.grid(row=1, column=0, sticky='NESW')
        self.leftFrameLower.grid(row=2, column=0, sticky='NESW')
        self.rightFrame.grid(row=1, column=1, rowspan=2, sticky='NESW')
        self.lowerFrame.grid(row=3, column=0, columnspan=2, sticky='NESW')

        self.get_seq_choices()

    # GUI METHODS
    def activate_chosen_frame(self):

        self.frames = (
            self.leftFrameUpper, # MainMenu = 1, index 0
            self.leftFrameLower, # MainMenu = 2, index 1
            self.rightFrame # MainMenu = 3, index 2
        )

        self.mainMenuButtons = (
            self.leftFrameUpper.ChooseRandom, # MainMenu = 1, index 0
            self.leftFrameLower.ChooseWordSequence, # MainMenu = 2, index 1
            self.rightFrame.ChooseCustomWord # MainMenu = 3, index 2
                                )

        for frame in self.frames:
            for child in frame.winfo_children():
                if child not in self.mainMenuButtons:
                    child.config(state="disabled")

        self.frameToEnable = self.frames[0]

        if self.MainMenu.get() == 1:
            self.frameToEnable = self.frames[0]

        elif self.MainMenu.get() == 2:
            self.frameToEnable = self.frames[1]

        elif self.MainMenu.get() == 3:
            self.frameToEnable = self.frames[2]

        for child in self.frameToEnable.winfo_children():
            child.config(state='normal')
            print(child)

    def activate_widget_group(self):
        pass

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

    def get_seq_choices(self):
        # print(self.leftFrameLower.numseq.get())
        pass


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

    # GENERAL:
    def display_password(self):

        self.password = self.generate_random_password()

        self.upperFrame.ThePassword.delete(0,'end')
        self.upperFrame.ThePassword.insert(0,self.password)




# COME TO LIFE

main = Main_Application(root)
main.grid(column = 0, row = 0, padx = 10, pady = 10)
tk.mainloop()