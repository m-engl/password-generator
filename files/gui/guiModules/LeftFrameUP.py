import tkinter as tk

class Left_Frame_UP(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.ChooseRandom = tk.Radiobutton(self, text="Generate random password",
                                           variable=self.master.MainMenu, value=1,
                                           command=self.master.activate_chosen_frame)
        self.ChooseRandom.grid(row=0, column=0, columnspan=4,
                               padx=5, pady=5,
                               sticky='W') #

        self.LabelEnterLength = tk.Label(self, text="Enter length: ")
        self.LabelEnterLength.grid(row=1, column=1,
                                   padx=(20, 5), pady=5,
                                   sticky='W')

        self.FieldEnterLength = tk.Entry(self, width=3, bg="snow2")  # , relief="solid", borderwidth=1
        self.FieldEnterLength.grid(row=1, column=2,
                                   padx=2, pady=2)

        self.EnterLengthOKButton = tk.Button(self, text="OK",
                                             height=1, width=4,
                                             command=self.master.get_length)
        self.EnterLengthOKButton.grid(row=1, column=3,
                                      padx=2, pady=2,
                                      sticky='W')

        self.LabelUserEnteredLength = tk.Label(self, text='0', fg='grey')
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
        for choice, description in self.master.strengthMODES:
            self.rb = tk.Radiobutton(self, text = description, variable = self.master.ChooseStrength, value = choice,
                                     command=lambda: print(variable, value))
            self.rb.grid(row = self.i, column=1, columnspan=4,
                         padx = (25, 5),
                         sticky='W')
            self.i += 1
