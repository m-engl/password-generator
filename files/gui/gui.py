import tkinter as tk
import random
import UpperFrame as Upper_Frame
import LeftFrameUP as Left_Frame_UP
import LeftFrameLOW as Left_Frame_LOW
import RightFrame as Right_Frame
import LowerFrame as Lower_Frame
import randomPwdGenerator as Random_Password_Generator
import sequence as Sequence_Based_Generator
import wordbased as Word_Based_Password

root = tk.Tk()

# VARIABLES
theTitle = "My ULTIMATE (PASS)WORD Generator"
theLogo = "img/logo.gif"

# Here comes the main application class

class Main_Application(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title(theTitle)
        self.logo = tk.PhotoImage(file=theLogo)
        self.MainMenu = tk.IntVar()
        # Main Menu:
        # random password 1
        # word sequence based 2
        # custom word/crazy word based 3
        # self.customWordChoice = tk.IntVar()
        # self.customWordMODES = customWordMODES
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

        # Password Generator modules
        self.Randy = Random_Password_Generator.Random_Password_Generator()
        self.Seqqe = Sequence_Based_Generator.Sequence_Based_Generator()
        self.Wordy = Word_Based_Password.Word_Based_Password()

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

    # GENERAL:
    def display_password(self):

        if self.MainMenu.get() == 1: # Random Password Generator activated

            length = int(self.leftFrameUpper.get_length())
            strength = self.leftFrameUpper.get_strength()

            self.password = self.Randy.generate_random_password(length, strength)

        elif self.MainMenu.get() == 2:  # Sequence-Based Password Generator activated
            sequence = self.leftFrameLower.get_sequence()
            choices = self.leftFrameLower.get_values_for_seqCHOICES()

            self.password = self.Seqqe.generate_sequence_based_password(sequence, choices)

        elif self.MainMenu.get() == 3:  # Word-Based Password Generator activated
            usersCustomWord = str(self.rightFrame.get_word())
            radiobuttonsChosen = self.rightFrame.get_WORD_choice_level1()
            mixChangeNumber = self.rightFrame.get_number_mixChange()
            howManySignsToAdd = self.rightFrame.get_number_addSigns()
            checkbuttonsChecked = self.rightFrame.get_WORD_choice_level2()


            self.password = self.Wordy.generate_word_based_password(theWord=usersCustomWord,
                                                                    choicesLevel1=radiobuttonsChosen,
                                                                    choicesLevel2=checkbuttonsChecked,
                                                                    numberMixChange=mixChangeNumber,
                                                                    numberAddSigns=howManySignsToAdd)

        else:
            self.password = "ERROR: You have not chosen any option!"

        self.upperFrame.ThePassword.delete(0, 'end')
        self.upperFrame.ThePassword.insert(0, str(self.password))




# COME TO LIFE

main = Main_Application(root)
main.grid(column = 0, row = 0, padx = 10, pady = 10)
tk.mainloop()