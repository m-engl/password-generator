import tkinter as tk

class Config:

    def __init__(self):

        # general
        self.mainmenu = 1

        # random
        self.length = 9
        self.choosestrength = 3

        # sequence
        self.sequence = "you pretty things"
        self.seqNum = 0
        self.seqSpec = 1
        self.seqMix = 1

        # word
        self.word = "peculiarity"
        self.customwordchoice = 1
        self.mixchangeHowMany = 2
        self.addsignsHowMany = 3
        self.wNum = 1
        self.wSpec = 1
        self.wMix = 0

        # LAYOUT
        # colours

        self.frameLine_thick = 1
        self.frameLine_colour  = "black"
        self.background = "azure3"
        self.passwordBg = "light goldenrod"
        self.entryBg = "ghost white"

    def set_bg_colour(self, master):

    # general backgroud:

        for child in master.winfo_children():

            if isinstance(child, (tk.Radiobutton, tk.Frame, tk.Checkbutton, tk.Label, tk.Button)):
                child.config(bg=self.background)

                for nextChild in child.winfo_children():
                    if isinstance(nextChild, (tk.Radiobutton, tk.Frame, tk.Checkbutton, tk.Label, tk.Button)):
                        nextChild.config(bg=self.background)

            for nextChild in child.winfo_children():
                if isinstance(nextChild, tk.Entry) and nextChild != master.upperFrame.ThePassword:
                    nextChild.config(bg=self.entryBg, disabledbackground=self.background)

                elif nextChild ==  master.upperFrame.ThePassword:
                    nextChild.config(bg=self.passwordBg, disabledbackground=self.background)



    # the password field backgroud:


    def set_default_text(self, text):
        e.delete(0, END)
        e.insert(0, text)


