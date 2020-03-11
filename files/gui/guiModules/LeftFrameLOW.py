import tkinter as tk

class Left_Frame_LOW(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.ChooseWordSequence = tk.Radiobutton(self, text="Word sequence-based password",
                                            variable=self.master.MainMenu, value=2,
                                           command=self.master.activate_chosen_frame)
        self.ChooseWordSequence.grid(row=0, column=0, columnspan=3,
                                padx=5, pady=5,
                                sticky='W')

        self.LabelEnterWordSequence = tk.Label(self, text="Enter words separated by spaces: ")
        self.LabelEnterWordSequence.grid(row=1, column=0, columnspan=3,
                                         padx=(20, 5), pady=(5),
                                         sticky='W')

        self.FieldEnterSequence = tk.Entry(self, width=28, bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterSequence.grid(row=2, column=0, columnspan=3,
                                     padx=(20, 5))

        self.EnterSequenceOKButton = tk.Button(self, text="OK", height = 1, width = 4,
                                        command=self.master.get_sequence)
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

        # Checkboxes

        self.num = tk.IntVar()
        self.spec = tk.IntVar()
        self.mix = tk.IntVar()

        self.checkNumbers = tk.Checkbutton(self, text=self.master.seqCHOICES[0], variable=self.num)
        self.checkNumbers.grid(row=6, column=1, columnspan=4,
                               sticky='W')

        self.checkSpecials = tk.Checkbutton(self, text=self.master.seqCHOICES[1], variable=self.spec)
        self.checkSpecials.grid(row=7, column=1, columnspan=4,
                                sticky='W')

        self.checkMixed = tk.Checkbutton(self, text=self.master.seqCHOICES[2], variable=self.mix)
        self.checkMixed.grid(row=8, column=1, columnspan=4,
                             sticky='W')


        # self.create_checkboxes_sequence(6) # arg: begin_with_row_number

    # def create_checkboxes_sequence(self, begin_with_row_number):
    #     self.i = begin_with_row_number
    #     for variableName, description in self.master.seqCHOICES:
    #         self.cb = tk.Checkbutton(self, text=description, variable=variableName)
    #         self.cb.grid(row=self.i, column=1, columnspan=4,
    #                      sticky='W')
    #         self.i += 1
