import tkinter as tk
import win32clipboard
import UpperFrame as Upper_Frame
import LeftFrameUP as Left_Frame_UP
import LeftFrameLOW as Left_Frame_LOW
import RightFrame as Right_Frame
import LowerFrame as Lower_Frame
import randomPwdGenerator as Random_Password_Generator
import sequence as Sequence_Based_Generator
import wordbased as Word_Based_Password
import config

root = tk.Tk()

# "GENERAL" VARIABLES
theTitle = "My ULTIMATE (PASS)WORD Generator"
theLogo = "img/logo.gif"

Main_Set = config.Config()

# MAIN APPLICATION
class Main_Application(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        # VARIABLES & SETTINGS:
        self.master = master
        master.title(theTitle)
        self.logo = tk.PhotoImage(file=theLogo)

        self.password = tk.StringVar()

        Set = config.Config()
        self.MainMenu = tk.IntVar()
        self.MainMenu.set(Set.mainmenu)
        self.sequence = tk.StringVar()
        self.sequence.set(Set.sequence)
        self.word = tk.StringVar()
        self.word.set(Set.word)

        # Password Generator modules:
        self.Randy = Random_Password_Generator.Random_Password_Generator()
        self.Seqqe = Sequence_Based_Generator.Sequence_Based_Generator()
        self.Wordy = Word_Based_Password.Word_Based_Password()

        # FRAMES
        self.upperFrame = Upper_Frame.Upper_Frame(self, highlightbackground=Set.frameLine_colour,
                                                  highlightthickness=Set.frameLine_thick)
        self.leftFrameUpper = Left_Frame_UP.Left_Frame_UP(self, highlightbackground=Set.frameLine_colour,
                                                          highlightthickness=Set.frameLine_thick)
        self.leftFrameLower = Left_Frame_LOW.Left_Frame_LOW(self, highlightbackground=Set.frameLine_colour,
                                                            highlightthickness=Set.frameLine_thick)
        self.rightFrame = Right_Frame.Right_Frame(self, highlightbackground=Set.frameLine_colour,
                                                  highlightthickness=Set.frameLine_thick)
        self.lowerFrame = Lower_Frame.Lower_Frame(self, highlightbackground=Set.frameLine_colour,
                                                  highlightthickness=Set.frameLine_thick)

        # LAYOUT
        self.upperFrame.grid(row=0, column=0, columnspan=2, sticky='NESW')
        self.leftFrameUpper.grid(row=1, column=0, sticky='NESW')
        self.leftFrameLower.grid(row=2, column=0, sticky='NESW')
        self.rightFrame.grid(row=1, column=1, rowspan=2, sticky='NESW')
        self.lowerFrame.grid(row=3, column=0, columnspan=2, sticky='NESW')



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

    # DISPLAY PASSWORD METHOD:
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

    # CLIPBOARD
    def copy_to_clipboard(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(self.upperFrame.ThePassword.get())
        win32clipboard.CloseClipboard()


# COME TO LIFE

main = Main_Application(root, highlightbackground=Main_Set.frameLine_colour, highlightthickness=Main_Set.frameLine_thick)
main.grid(column = 0, row = 0)
main.activate_chosen_frame()
Main_Set.set_bg_colour(main)
main.leftFrameUpper.get_length()
main.leftFrameUpper.get_strength()
main.leftFrameLower.get_sequence()
main.rightFrame.get_word()


tk.mainloop()