import tkinter as tk
import valuemethods
import config

class Right_Frame(tk.Frame):

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        Values = valuemethods.Value_Action()

        # VARS & SETTINGS:
        Set = config.Config()

        self.numberAddSigns = int()
        self.numberAddSigns = Set.addsignsHowMany
        self.numberMixChange = int()
        self.numberMixChange = Set.mixchangeHowMany
        self.customWordChoice = tk.IntVar()
        self.customWordChoice.set(Set.customwordchoice)

        self.num = tk.IntVar()
        self.spec = tk.IntVar()
        self.mix = tk.IntVar()
        self.num.set(Set.wNum)
        self.spec.set(Set.wSpec)
        self.mix.set(Set.wMix)



        self.customWordMODES = [
    (1, "Mix case randomly"),
    (2, "Change all the letters to look-alike\nnumbers and special characters"),
    (3, "Mix case and change a chosen number \nof letters to special characters and/or numbers"),
    (4, "Add a chosen number of special characters and/or\nnumbers in between the word's letters")
            ]

        self.addChars = ["numbers", "special characters", "mixed case"]

        self.ChooseCustomWord = tk.Radiobutton(self, text="\"Crazy word\" password",
                                       variable=self.master.MainMenu, value=3,
                                       justify="left",
                                           command=lambda: [self.master.activate_chosen_frame(),
                                                            self.enable_suboptions_set(Set.customwordchoice)])
        self.ChooseCustomWord.grid(row=0, column=0, columnspan=5,
                                  padx=(0, 5),
                                   sticky='W')

        # AREA FOR ENTERING THE CUSTOM WORD:
        self.LabelEnterWord = tk.Label(self, text="Enter your word:")
        self.LabelEnterWord.grid(row=1, column=0,
                                 padx=(20, 5), pady=(5),
                                 sticky='W')

        self.FieldEnterWord = tk.Entry(self, width=20, bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterWord.grid(row=1, column=1,  columnspan=2,
                                 padx=(5, 2),
                                 sticky='W')
        self.FieldEnterWord.insert(0, Set.word)

        # self.EnterWordOKButton = tk.Button(self, text="OK",
        #                                    height=1, width=4,
        #                                    command=self.get_word)
        # self.EnterWordOKButton.grid(row=1, column=3,
        #                             padx=(2, 2),
        #                             sticky='W')
        #
        # self.LabelUserEnteredWord = tk.Label(self, text='peculiar', # change text to user input
        #                                      fg='grey')
        # self.LabelUserEnteredWord.grid(row=2, column=1,
        #                                padx=2, pady=2,
        #                                sticky='W')

        self.LabelMenuWord = tk.Label(self, text='Choose your options:')
        self.LabelMenuWord.grid(row=3, column=0, columnspan=5,
                                padx=(25, 5), pady=(5),
                                sticky='W')
        #RADIO BUTTONS ROW 4-5-6
        self.create_radios_custom_word(4) # begin_with_row_number

        self.LabelEnterHowMany_mixChange = tk.Label(self,
            text="Enter how many letters you want\nto have changed to \"look-alikes\": ",
            justify="left")
        self.LabelEnterHowMany_mixChange.grid(row=7, column=0, columnspan=2,
                                         padx=(45, 5),
                                         sticky='W')

        self.FieldEnterHowMany_mixChange = tk.Entry(self, width=3,
                                                   bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterHowMany_mixChange.grid(row=7, column=2,
                                              padx=5, pady=2)
        self.FieldEnterHowMany_mixChange.insert(0, self.numberMixChange)

        self.PlusButton_mixChange = tk.Button(self, text='+',width=2,
                                    command=lambda: Values.increment(self.numberMixChange,
                                                                     self.FieldEnterHowMany_mixChange))
        self.MinusButton_mixChange = tk.Button(self, text='-',width=2,
                                     command=lambda: Values.decrement(self.numberMixChange,
                                                                      self.FieldEnterHowMany_mixChange))

        self.PlusButton_mixChange.grid(row=7, column=3,
                                      padx=2, pady=2,
                                      sticky='W')
        self.MinusButton_mixChange.grid(row=7, column=4,
                                         padx=2, pady=2,
                                         sticky='W')

        # self.EnterHowManyOKButton_mixChange = tk.Button(self, text="OK",
        #                                                 height=1, width=4,
        #                                                 command=self.get_number_mixChange)
        # self.EnterHowManyOKButton_mixChange.grid(row=7, column=3,
        #                                          padx=2, pady=2,
        #                                          sticky='W')
        #
        # self.LabelUserEnteredHowMany_mixChange = tk.Label(self, text='2', fg='grey')
        # self.LabelUserEnteredHowMany_mixChange.grid(row=7, column=4,
        #                                             padx=2, pady=2,
        #                                             sticky='W')

        # RADIO BUTTONS ROW 11 here
        # next

        self.LabelEnterHowMany_addSigns = tk.Label(self,
            text="How many new signs do you want to add? ",
            justify="left")
        self.LabelEnterHowMany_addSigns.grid(row=12, column=0, columnspan=2,
                                             padx=(45, 5),
                                             sticky='W')

        self.FieldEnterHowMany_addSigns = tk.Entry(self, width=3,
                                                   bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterHowMany_addSigns.grid(row=12, column=2,
                                              padx=5, pady=2)
        self.FieldEnterHowMany_addSigns.insert(0, self.numberAddSigns)

        self.PlusButton_addSigns = tk.Button(self, text='+', width=2,
                                    command=lambda: Values.increment(self.numberAddSigns,
                                                                     self.FieldEnterHowMany_addSigns))
        self.MinusButton_addSigns = tk.Button(self, text='-', width=2,
                                    command=lambda: Values.decrement(self.numberAddSigns,
                                                                     self.FieldEnterHowMany_addSigns))

        self.PlusButton_addSigns.grid(row=12, column=3,
                                      padx=2, pady=2,
                                      sticky='W')
        self.MinusButton_addSigns.grid(row=12, column=4,
                                         padx=2, pady=2,
                                         sticky='W')

        # self.EnterHowManyOKButton_addSigns = tk.Button(self, text="OK",
        #                                                 height=1, width=4,
        #                                                command=self.get_number_addSigns)
        # self.EnterHowManyOKButton_addSigns.grid(row=12, column=3,
        #                                          padx=2, pady=2,
        #                                          sticky='W')
        #
        # self.LabelUserEnteredHowMany_addSigns = tk.Label(self, text='2', fg='grey')
        # self.LabelUserEnteredHowMany_addSigns.grid(row=12, column=4,
        #                                             padx=2, pady=2,
        #                                             sticky='W')

        self.LabelUse = tk.Label(self, text='Use:')
        self.LabelUse.grid(row=13, column=0, columnspan=4,
                           padx=55, pady=2,
                           sticky='W')

        # Checkboxes


        self.checkNumbers = tk.Checkbutton(self, text=self.addChars[0], variable=self.num)
        self.checkNumbers.grid(row=14, column=0, columnspan=4,
                                 padx=60,
                                 sticky='W')

        self.checkSpecials = tk.Checkbutton(self, text=self.addChars[1], variable=self.spec)
        self.checkSpecials.grid(row=15, column=0, columnspan=4,
                                 padx=60,
                                 sticky='W')

        self.checkMixed = tk.Checkbutton(self, text=self.addChars[2], variable=self.mix)
        self.checkMixed.grid(row=16, column=0, columnspan=4,
                             padx=60,
                             sticky='W')

        # SUB-OPTION WIDGET SETS:
        # These are activated when suitable

        # activated only on choice of self.customWordChoice=3
        self.mixChangeWidgets = [
            self.LabelEnterHowMany_mixChange,
            self.FieldEnterHowMany_mixChange,
            self.PlusButton_mixChange,
            self.MinusButton_mixChange
        ]

        # activated only on choice of self.customWordChoice=4
        self.addSignsWidgets = [
            self.LabelEnterHowMany_addSigns,
            self.FieldEnterHowMany_addSigns,
            self.PlusButton_addSigns,
            self.MinusButton_addSigns,
            self.LabelUse,
            self.checkNumbers,
            self.checkSpecials,
            self.checkMixed
        ]


    # METHODS:
    def create_radios_custom_word(self, begin_with_row_number):

        def create_radios_cword():
            self.rb = tk.Radiobutton(self, text=description,
                                     variable=self.customWordChoice, value=mode,
                                     justify="left",
                                     command=lambda: self.enable_suboptions_set(self.customWordChoice.get()))
            self.rb.grid(row=self.i, column=0, columnspan=5,
                         padx=(25, 25), pady=2,
                         sticky='W')
            return self.rb

        self.i = begin_with_row_number

        for mode, description in self.customWordMODES:

            if mode in range(1, 4):
                create_radios_cword()
                self.i += 1

            elif mode == 4:
                self.i = 11
                create_radios_cword()

    def enable_suboptions_set(self, subset):

        allSuboptions = self.mixChangeWidgets + self.addSignsWidgets

        if subset == 3:

            for widget in self.addSignsWidgets:
                widget.config(state="disabled")

            for widget in self.mixChangeWidgets:
                widget.config(state="normal")

        elif subset == 4:

            for widget in self.mixChangeWidgets:
                widget.config(state="disabled")

            for widget in self.addSignsWidgets:
                widget.config(state="normal")

        else:
            for widget in allSuboptions:
                widget.config(state="disabled")

    def get_word(self):
        self.word = self.FieldEnterWord.get()
        # self.LabelUserEnteredWord.config(text=str(self.word))
        return str(self.word)

    def get_number_mixChange(self):
        self.numberMixChange = self.FieldEnterHowMany_mixChange.get()
        # self.LabelUserEnteredHowMany_mixChange.config(text = str(self.numberMixChange))
        return self.numberMixChange

    def get_number_addSigns(self):
        self.numberAddSigns = self.FieldEnterHowMany_addSigns.get()
        # self.LabelUserEnteredHowMany_addSigns.config(text = str(self.numberAddSigns))
        return self.numberAddSigns

    def get_WORD_choice_level1(self): # from Radiobuttons
        self.level1choiceWORD = self.customWordChoice.get()  # 1, 2, 3 or 4
        return self.level1choiceWORD

    def get_WORD_choice_level2(self): # from the submenus for Radiobutton 3 and 4
        self.choices = list()
        self.choices.append(self.num.get())
        self.choices.append(self.spec.get())
        self.choices.append(self.mix.get())
        return self.choices