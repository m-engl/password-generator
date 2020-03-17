class Config:

    def __init__(self):

        self.word = "peculiarity"
        self.sequence = "you pretty things"
        self.mainmenu = 1
        self.length = 9
        self.mixchangeHowMany = 2
        self.addsignsHowMany = 3
        self.choosestrength = 3
        self.seqNum = 0
        self.seqSpec = 1
        self.seqMix = 1
        self.customwordchoice = 1
        self.wNum = 1
        self.wSpec = 1
        self.wMix = 0




    def set_default_text(self, text):
        e.delete(0, END)
        e.insert(0, text)


