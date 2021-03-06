import tkinter as tk
import config
import valuemethods

class Left_Frame_UP(tk.Frame):

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        # VARS & SETTINGS

        Set = config.Config()
        Values = valuemethods.Value_Action()

        self.length = int()
        self.length = Set.length
        self.ChooseStrength = tk.IntVar()
        self.ChooseStrength.set(Set.choosestrength)

        self.strengthMODES = [
                (1, "Weak"),
                (2, "Medium"),
                (3, "Strong"),
                (4, "Superstrong")
         ]

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

        self.FieldEnterLength = tk.Entry(self, width=3)  # , relief="solid", borderwidth=1
        self.FieldEnterLength.grid(row=1, column=2,
                                   padx=2, pady=2)
        self.FieldEnterLength.insert(0, self.length)

        self.PlusButton = tk.Button(self, text='+', width=2,
                                    command=lambda: Values.increment(self.length, self.FieldEnterLength))
        self.MinusButton = tk.Button(self, text='-', width=2,
                                     command=lambda: Values.decrement(self.length, self.FieldEnterLength))

        self.PlusButton.grid(row=1, column=3, sticky='W')
        self.MinusButton.grid(row=1, column=4, sticky='W')

        # self.EnterLengthOKButton = tk.Button(self, text="OK",
        #                                      height=1, width=4,
        #                                      command=self.get_length)
        # self.EnterLengthOKButton.grid(row=1, column=3,
        #                               padx=2, pady=2,
        #                               sticky='W')
        #
        # self.LabelUserEnteredLength = tk.Label(self, text='0', fg='grey')
        # self.LabelUserEnteredLength.grid(row=1, column=4,
        #                                  padx=2, pady=2,
        #                                  sticky='W')

        self.LabelChooseStrength = tk.Label(self, text='Choose strength:')
        self.LabelChooseStrength.grid(row=2, column=1,
                                 padx=(25, 5), pady=2,
                                 sticky='W')

        self.create_radios_strength(3)  # argument: begin_with_row_number

    def create_radios_strength(self, begin_with_row_number):
        self.i = begin_with_row_number
        for choice, description in self.strengthMODES:
            self.rb = tk.Radiobutton(self, text=description, variable=self.ChooseStrength, value=choice)
            self.rb.grid(row=self.i, column=1, columnspan=4,
                         padx=(25, 5),
                         sticky='W')
            self.i += 1

    # # +/- BUTTON METHODS
    #
    # def increment(self):
    #     self.length = int(self.length)
    #     self.length += 1
    #     self.length = str(self.length)
    #     self.FieldEnterLength.delete(0, 'end')
    #     self.FieldEnterLength.insert(0, self.length)
    #
    # def decrement(self):
    #     self.length = int(self.length)
    #     self.length -= 1
    #     self.length = str(self.length)
    #     self.FieldEnterLength.delete(0, 'end')
    #     self.FieldEnterLength.insert(0, self.length)

    # GET VALUES

    def get_length(self):
        self.length = self.FieldEnterLength.get()
        # self.LabelUserEnteredLength.config(text = str(self.length))
        return self.length

    def get_strength(self):
        self.strength = self.ChooseStrength.get() # 1, 2, 3 or 4
        return self.strength