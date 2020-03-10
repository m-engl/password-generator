import tkinter as tk
root = tk.Tk()

# VARIABLES
theTitle = "My ULTIMATE (PASS)WORD Generator"
logo = tk.PhotoImage(file="img/logo.gif")

MainMenu = tk.IntVar()
# Main Menu:
# random password 1
# word sequence based 2
# custom word/crazy word based 3

ChooseStrength = tk.IntVar()

strengthMODES = [
    (1, "Weak"),
    (2, "Medium"),
    (3, "Strong"),
    (4, "Superstrong")
]

seqCHOICES = [
    ("numseq", "numbers"),
    ("specseq", "special characters"),
    ("mixseq", "mixed case")
]

addSpecialsCHOICES = seqCHOICES

customWordChoice = tk.IntVar()
customWordChoice.set(1)

customWordMODES = [
    (1, "Mix case randomly"),
    (2, "Change all the letters to look-alike\nnumbers and special characters"),
    (3, "Mix case and change a chosen number \nof letters to special characters and/or numbers"),
    (4, "Add a chosen number of special characters and/or\nnumbers in between the word's letters")
]

# CLASSES - fRAMES (for the main frames) that are to be put together in the Main_Application

class Upper_Frame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.Logo = tk.Label(self, image=logo)
        self.Logo.grid(row=0, column=0, rowspan=3,
                       padx=5, pady=5)

        self.TextBegin = tk.Label(self, text="Before generating the password, choose your options below.")
        self.TextBegin.grid(row=4, column=0, columnspan=5,
                            padx=10, pady=2,
                            sticky='W')

        self.GenPassButton = tk.Button(self, text="Generate",
                                       width = 12, height=2)
        self.GenPassButton.grid(row=2, column=1, rowspan=2,
                                padx=5, pady=5)

        self.YourNewPasswordIs = tk.Label(self, text="Your new password is:")
        self.YourNewPasswordIs.grid(row=1, column=2,
                                    padx=5, pady=(5,1),
                                    sticky='S')

        self.ThePassword = tk.Text(self, height=1, width=35, bg="light goldenrod")  # , relief="solid", borderwidth=1
        self.ThePassword.grid(row=2, column=2, rowspan=2)

        self.CopyButton = tk.Button(self, text="Copy")
        self.CopyButton.grid(row=2, column=3, rowspan=2,
                             padx=5, pady=1)


class Left_Frame_UP(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.ChooseRandom = tk.Radiobutton(self, text="Generate random password",
                                           variable=MainMenu, value=1,
                                           command=self.master.activate_chosen_frame)
        self.ChooseRandom.grid(row=0, column=0, columnspan=4,
                               padx=5, pady=5,
                               sticky='W') #

        self.LabelEnterLength = tk.Label(self, text="Enter length: ")
        self.LabelEnterLength.grid(row=1, column=1,
                                   padx=(20, 5), pady=5,
                                   sticky='W')

        self.FieldEnterLength = tk.Text(self, height=1, width=3, bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterLength.grid(row=1, column=2,
                                   padx=2, pady=2)

        self.EnterLengthOKButton = tk.Button(self, text="OK", height=1, width=4)
        self.EnterLengthOKButton.grid(row=1, column=3,
                                      padx=2, pady=2,
                                      sticky='W')

        self.LabelUserEnteredLength = tk.Label(self, text='12', fg='grey')
        self.LabelUserEnteredLength.grid(row=1, column=4,
                                         padx=2, pady=2,
                                         sticky='W')

        self.LabelChooseStrength = tk.Label(self, text='Choose strength:')
        self.LabelChooseStrength.grid(row=2, column=1,
                                 padx=(25, 5), pady=2,
                                 sticky='W')

        self.create_radios_strength(3)  # argument: begin_with_row_number

    def create_radios_strength(self, begin_with_row_number):
        self.i = begin_with_row_number
        for choice, description in strengthMODES:
            self.rb = tk.Radiobutton(self, text = description, variable = ChooseStrength, value = choice)
            self.rb.grid(row = self.i, column=1, columnspan=4,
                         padx = (25, 5),
                         sticky='W')
            self.i += 1


class Left_Frame_LOW(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.ChooseWordSequence = tk.Radiobutton(self, text="Word sequence-based password",
                                            variable=MainMenu, value=2,
                                           command=self.master.activate_chosen_frame)
        self.ChooseWordSequence.grid(row=0, column=0, columnspan=3,
                                padx=5, pady=5,
                                sticky='W')

        self.LabelEnterWordSequence = tk.Label(self, text="Enter words separated by spaces: ")
        self.LabelEnterWordSequence.grid(row=1, column=0, columnspan=3,
                                         padx=(20, 5), pady=(5),
                                         sticky='W')

        self.FieldEnterSequence = tk.Text(self, height=1, width=28, bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterSequence.grid(row=2, column=0, columnspan=3,
                                     padx=(20, 5))

        self.EnterSequenceOKButton = tk.Button(self, text="OK", height = 1, width = 4)
        self.EnterSequenceOKButton.grid(row=3, column=1, columnspan = 3,
                                        padx=(20, 30),
                                        sticky='W')

        self.LabelUserEnteredSequence = tk.Label(self, text='cat wants food', fg='grey')
        self.LabelUserEnteredSequence.grid(row=3, column=2,
                                           padx=2, pady=2,
                                           sticky='W')

        self.LabelMenuSequence = tk.Label(self, text='Use:')
        self.LabelMenuSequence.grid(row=5, column=1,
                               padx=(25, 5), pady=(5),
                               sticky='W')

        self.create_checkboxes_sequence(6) # arg: begin_with_row_number

    def create_checkboxes_sequence(self, begin_with_row_number):
        self.i = begin_with_row_number
        for variableName, description in seqCHOICES:
            variableName = tk.IntVar()
            self.cb = tk.Checkbutton(self, text=description, variable=variableName)
            self.cb.grid(row=self.i, column=1, columnspan=4,
                         sticky='W')
            self.i += 1


class Right_Frame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.ChooseCustomWord = tk.Radiobutton(self, text="\"Crazy word\" password",
                                       variable=MainMenu, value=3,
                                       justify="left",
                                           command=self.master.activate_chosen_frame)
        self.ChooseCustomWord.grid(row=0, column=0, columnspan=5,
                                  padx=(0, 5),
                                   sticky='W')

        # CUSTOM WORD ENTER and confirm

        self.LabelEnterWord = tk.Label(self, text="Enter your word:")
        self.LabelEnterWord.grid(row=1, column=0,
                                 padx=(20, 5), pady=(5),
                                 sticky='W')

        self.FieldEnterWord = tk.Text(self,
                                   height=1, width=20,
                                   bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterWord.grid(row=1, column=1,  columnspan=2,
                                 padx=(5, 2),
                                 sticky='W')

        self.EnterWordOKButton = tk.Button(self, text="OK",
                                        height=1, width=4)
        self.EnterWordOKButton.grid(row=1, column=3,
                                    padx=(2, 2),
                                    sticky='W')

        self.LabelUserEnteredWord = tk.Label(self, text='peculiar', # change text to user input
                                             fg='grey')
        self.LabelUserEnteredWord.grid(row=2, column=1,
                                       padx=2, pady=2,
                                       sticky='W')

        self.LabelMenuWord = tk.Label(self, text='Choose your options:')
        self.LabelMenuWord.grid(row=3, column=0, columnspan=5,
                                padx=(25, 5), pady=(5),
                                sticky='W')

        self.create_radios_custom_word(4) # begin_with_row_number

        self.LabelEnterHowMany_mixChange = tk.Label(self,
            text="Enter how many letters you want\nto have changed to \"look-alikes\": ",
            justify="left")
        self.LabelEnterHowMany_mixChange.grid(row=7, column=0, columnspan=2,
                                         padx=(45, 5),
                                         sticky='W')

        self.FieldEnterHowMany_mixChange = tk.Text(self, height=1, width=3,
                                                   bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterHowMany_mixChange.grid(row=7, column=2,
                                              padx=5, pady=2)

        self.EnterHowManyOKButton_mixChange = tk.Button(self, text="OK",
                                                        height=1, width=4)
        self.EnterHowManyOKButton_mixChange.grid(row=7, column=3,
                                                 padx=2, pady=2,
                                                 sticky='W')

        self.LabelUserEnteredHowMany_mixChange = tk.Label(self, text='2', fg='grey')
        self.LabelUserEnteredHowMany_mixChange.grid(row=7, column=4,
                                                    padx=2, pady=2,
                                                    sticky='W')

        self.LabelUse = tk.Label(self, text='Use:')
        self.LabelUse.grid(row=13, column=0, columnspan=4,
                           padx=55, pady=2,
                           sticky='W')

        self.create_checkboxes_custom_word(14) # begin_with_row_number




    # METHODS:
    def create_radios_custom_word(self, begin_with_row_number):

        def create_radios_cword():
            self.rb = tk.Radiobutton(self, text=description,
                                     variable=customWordChoice, value=mode,
                                     justify="left")
            self.rb.grid(row=self.i, column=0, columnspan=5,
                         padx=(25, 25), pady=2,
                         sticky='W')
            return self.rb

        self.i = begin_with_row_number

        for mode, description in customWordMODES:
            if mode == 4:
                self.i = 11
                create_radios_cword()

            elif mode in range(1, 4):
                create_radios_cword()
                self.i += 1

    def create_checkboxes_custom_word(self, begin_with_row_number):
        self.i = begin_with_row_number
        for variableName, description in addSpecialsCHOICES:
            variableName = tk.IntVar()
            self.cb = tk.Checkbutton(self, text=description,
                                     variable=variableName,
                                     anchor='w')
            self.cb.grid(row=self.i, column=0, columnspan=4,
                         padx=60,
                         sticky='W')
            self.i += 1


class Lower_Frame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.author = tk.Label(self,
                            text="Author: M.E. \nAll rights reserverd. \nSuggestions? Contact me(hyperlink)")
        self.author.grid(column=0, row=0,
                         padx=80, pady=5,
                         sticky='E'
                         )

        self.HelpButton = tk.Button(self, text="HELP",
                                 width=4, height=1)
        self.HelpButton.grid(column=1, row=0,
                             padx=(60, 5),
                             sticky='E')

# MAIN APP-CLASS

class Main_Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title(theTitle)

        # FRAMES
        self.upperFrame = Upper_Frame(self, highlightbackground="black", highlightthickness=1)
        self.leftFrameUpper = Left_Frame_UP(self, highlightbackground="black", highlightthickness=1)  #
        self.leftFrameLower = Left_Frame_LOW(self, highlightbackground="black", highlightthickness=1)  #
        self.rightFrame = Right_Frame(self, highlightbackground="black", highlightthickness=1)  #
        self.lowerFrame = Lower_Frame(self, highlightbackground="black", highlightthickness=1)

        # LAYOUT
        self.upperFrame.grid(row=0, column=0, columnspan=2, sticky='NESW')
        # upperFrame.grid_propagate(False) # used to never resize the frame if it g
        self.leftFrameUpper.grid(row=1, column=0, sticky='NESW')
        self.leftFrameLower.grid(row=2, column=0, sticky='NESW')
        self.rightFrame.grid(row=1, column=1, rowspan=2, sticky='NESW')
        self.lowerFrame.grid(row=3, column=0, columnspan=2, sticky='NESW')


    # GUI METHODS
    # def disable_nonchosen_frames(self):
    #
    #     self.framesToDisable = ()
    #
    #     self.frames = (
    #         self.leftFrameUpper, # MainMenu = 1, index 0
    #         self.leftFrameLower, # MainMenu = 2, index 1
    #         self.rightFrame # MainMenu = 3, index 2
    #     )
    #
    #     self.mainMenuButtons = (
    #         self.leftFrameUpper.ChooseRandom, # MainMenu = 1, index 0
    #         self.leftFrameLower.ChooseWordSequence, # MainMenu = 2, index 1
    #         self.rightFrame.ChooseCustomWord # MainMenu = 3, index 2
    #                             )
    #
    #     if MainMenu.get() == 1:
    #         self.framesToDisable = (self.frames[1], self.frames[2])
    #
    #     elif MainMenu.get() == 2:
    #         self.framesToDisable = (self.frames[0], self.frames[2])
    #
    #     elif MainMenu.get() == 3:
    #         self.framesToDisable = (self.frames[0], self.frames[1])
    #
    #     for frame in self.framesToDisable:
    #         for child in frame.winfo_children():
    #             if child not in self.mainMenuButtons:
    #                 child.config(state='disabled')

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

        if MainMenu.get() == 1:
            self.frameToEnable = self.frames[0]

        elif MainMenu.get() == 2:
            self.frameToEnable = self.frames[1]

        elif MainMenu.get() == 3:
            self.frameToEnable = self.frames[2]

        for child in self.frameToEnable.winfo_children():
            child.config(state='normal')
            print(child)






# COME TO LIFE

main = Main_Application(root)
main.grid(column = 0, row = 0, padx = 10, pady = 10)






# main loop
tk.mainloop()