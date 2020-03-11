import tkinter as tk

seqCHOICES = [
    ("numseq", "numbers"),
    ("specseq", "special characters"),
    ("mixseq", "mixed case")
]


def create_checkboxes_sequence(begin_with_row_number):
    i = begin_with_row_number
    for variableName, description in seqCHOICES:
        states = []
        var = tk.IntVar()
        self.cb = tk.Checkbutton(self, text=description, variable=var)
        self.cb.pack()
        i += 1
        states.append(var.get())
        self.states = states


class FrameFrameFrame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.seqCHOICES = seqCHOICES
        self.states = []
        self.create_checkboxes_sequence(0)

        self.button = tk.Button(self, text='Click', command=self.read_values)
        self.button.pack()

        self.label = tk.Label(self,text=read_values())
        self.label.pack()









root = tk.Tk()
frame = FrameFrameFrame(root)
frame.pack()
print([var for var in frame.states])
tk.mainloop()
