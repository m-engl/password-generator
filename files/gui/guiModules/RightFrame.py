import tkinter as tk

class Right_Frame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.ChooseCustomWord = tk.Radiobutton(self, text="\"Crazy word\" password",
                                       variable=self.master.MainMenu, value=3,
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

        self.FieldEnterWord = tk.Entry(self, width=20, bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterWord.grid(row=1, column=1,  columnspan=2,
                                 padx=(5, 2),
                                 sticky='W')

        self.EnterWordOKButton = tk.Button(self, text="OK",
                                           height=1, width=4,
                                           command=self.master.get_word)
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
                                     variable=self.master.customWordChoice, value=mode,
                                     justify="left")
            self.rb.grid(row=self.i, column=0, columnspan=5,
                         padx=(25, 25), pady=2,
                         sticky='W')
            return self.rb

        self.i = begin_with_row_number

        for mode, description in self.master.customWordMODES:
            if mode == 4:
                self.i = 11
                create_radios_cword()

            elif mode in range(1, 4):
                create_radios_cword()
                self.i += 1

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
