import tkinter as tk
import webbrowser

class Lower_Frame(tk.Frame):

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.author = tk.Label(self,
                            text="Author: Magdalena Englart \nAll rights reserverd.")
        self.contact = tk.Label(self,
                                text=">> Contact me <<", cursor="hand2")
        self.contact.bind("<Button-1>", lambda e: webbrowser.open("mailto:m.englart@gmail.com", new=1))
        self.author.grid(column=0, row=0,
                         padx=80, pady=(5,1),
                         sticky='E'
                         )
        self.contact.grid(column=0, row=1,
                         padx=0, pady=(1,5),
                         sticky='nsew'
                         )

        self.HelpButton = tk.Button(self, text="HELP",
                                 width=4, height=1,
                                 command=lambda: webbrowser.open("help.html"))
        self.HelpButton.grid(column=1, row=0, rowspan=2,
                             padx=(60, 5),
                             sticky='E')
