import tkinter as tk
import config

class Left_Frame_LOW(tk.Frame):

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        # VARS & SETTINGS
        Set = config.Config()
        self.sequence = Set.sequence

        self.num = tk.IntVar()
        self.spec = tk.IntVar()
        self.mix = tk.IntVar()
        self.num.set(Set.seqNum)
        self.spec.set(Set.seqSpec)
        self.mix.set(Set.seqMix)

        self.seqCHOICES = ["numbers", "special characters", "mixed case"]


        # WIDGETS
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

        self.FieldEnterSequence = tk.Entry(self, width=30)  # , relief="solid", borderwidth=1
        self.FieldEnterSequence.grid(row=2, column=0, columnspan=2,
                                     padx=(25, 10))
        self.FieldEnterSequence.insert(0, self.sequence)

        # self.EnterSequenceOKButton = tk.Button(self, text="OK", height = 1, width = 4,
        #                                        command=self.get_sequence)
        # self.EnterSequenceOKButton.grid(row=3, column=1, columnspan = 3,
        #                                 padx=(20, 30),
        #                                 sticky='W')
        #
        # self.LabelUserEnteredSequence = tk.Label(self, text='cat wants food', fg='grey')
        # self.LabelUserEnteredSequence.grid(row=3, column=2,
        #                                    padx=2, pady=2,
        #                                    sticky='W')

        self.LabelMenuSequence = tk.Label(self, text='Use:', justify="left")
        self.LabelMenuSequence.grid(row=5, column=0,
                               padx=(20, 5), pady=(5),
                               sticky='W')

        # Checkboxes

        self.checkNumbers = tk.Checkbutton(self, text=self.seqCHOICES[0], variable=self.num)
        self.checkNumbers.grid(row=6, column=1, sticky='W')

        self.checkSpecials = tk.Checkbutton(self, text=self.seqCHOICES[1], variable=self.spec)
        self.checkSpecials.grid(row=7, column=1, sticky='W')

        self.checkMixed = tk.Checkbutton(self, text=self.seqCHOICES[2], variable=self.mix)
        self.checkMixed.grid(row=8, column=1, sticky='W')

    # METHODS
    def get_sequence(self):
        self.sequence = self.FieldEnterSequence.get()
        # self.LabelUserEnteredSequence.config(text=str(self.sequence))
        return self.sequence

    def get_values_for_seqCHOICES(self):
        self.choices = list()
        self.choices.append(self.num.get())
        self.choices.append(self.spec.get())
        self.choices.append(self.mix.get())
        return self.choices


