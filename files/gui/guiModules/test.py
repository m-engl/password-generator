import tkinter as tk

seqCHOICES = [
    ("num", "numbers"),
    ("spec", "special characters"),
    ("mix", "mixed case")
]





class FrameFrameFrame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.seqCHOICES = seqCHOICES
        self.states = []
        # self.create_checkboxes_sequence(0)

        self.button = tk.Button(self, text='Click', command=self.read_values)
        self.button.pack()

        self.label = tk.Label(self,text='wait')
        self.label.pack()

        self.num = tk.IntVar()
        self.spec = tk.IntVar()
        self.mix = tk.IntVar()

        self.cb = tk.Checkbutton(self, text=seqCHOICES[0][1], variable=self.num)
        self.cb.pack()

        self.cb = tk.Checkbutton(self, text=seqCHOICES[1][1], variable=self.spec)
        self.cb.pack()

        self.cb = tk.Checkbutton(self, text=seqCHOICES[2][1], variable=self.mix)
        self.cb.pack()



    #
    # def create_checkboxes_sequence(self, begin_with_row_number):
    #     i = begin_with_row_number
    #     for variableName, description in seqCHOICES:
    #         states = []
    #         var = tk.IntVar()
    #         self.cb = tk.Checkbutton(self, text=description, variable=var)
    #         self.cb.pack()
    #         i += 1
    #         states.append(var.get())
    #         self.states = states

    def read_values(self):
        print(self.num.get(),self.spec.get(),self.mix.get())



root = tk.Tk()
frame = FrameFrameFrame(root)
frame.pack()
# print([var for var in frame.states])
tk.mainloop()
