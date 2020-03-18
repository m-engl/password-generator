class Config:

    def __init__(self):

        # general
        self.mainmenu = 1

        # random
        self.length = 9
        self.choosestrength = 2

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

    def set_default_text(self, text):
        e.delete(0, END)
        e.insert(0, text)


