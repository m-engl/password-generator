import tkinter as tk

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
