from tkinter import *

root = Tk()
root.title('My Ultimate Password Generator')

# important variables
# MAIN MENU GROUP
MainMenu = IntVar()


# CREATE FRAMES
upperFrame = Frame(root, height=100, width=630) # , highlightbackground="black", highlightthickness=1
leftFrameUpper = Frame(root, height=200, width=270) # , highlightbackground="black", highlightthickness=1
leftFrameLower = Frame(root, height=250, width=270) # , highlightbackground="black", highlightthickness=1
rightFrame = Frame(root, height=450, width=360) # , highlightbackground="black", highlightthickness=1
lowerFrame = Frame(root, height=40, width=630) # , highlightbackground="black", highlightthickness=1

# PLACE FRAMES
upperFrame.grid(row=0, column=0, columnspan=2)
# upperFrame.grid_propagate(False) # used to never resize the frame
leftFrameUpper.grid(row=1, column=0)
leftFrameLower.grid(row=2, column=0)
rightFrame.grid(row=1, column=1, rowspan = 2)
lowerFrame.grid(row=3, column=0, columnspan=2)

# INSIDE THE UPPER FRAME upperFrame

# LOGO - the label is the working version,
# later there is going to be an image
# about h=60 and w=120 px, right now it is text units as
# when stuff contain text, h and w are in text units

# Logo = Label(upperFrame, text="LOGO", height = 6, width = 10, relief=RIDGE)
# Logo.grid(row=0, column=0, rowspan=3, padx=10, pady=5)

logo = PhotoImage(file="logo.gif")
Logo = Label(upperFrame, image=logo)
Logo.grid(row=0, column=0, rowspan=3, padx=10, pady=5)

TextBegin = Label(upperFrame, text="Before generating the password, choose your options below.")
TextBegin.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

GenPassButton = Button(upperFrame, text="Generate\nPassword")
GenPassButton.grid(row=1, column=1, padx=5, pady=5)

YourNewPasswordIs = Label(upperFrame, text="Your new password is:")
YourNewPasswordIs.grid(row=0, column=2, padx=5, pady=1)

ThePassword = Text(upperFrame, height=1, width = 35)
ThePassword.grid(row=1, column=2)

CopyButton = Button(upperFrame, text="Copy")
CopyButton.grid(row=2, column=2, padx=5, pady=1)

HelpButton = Button(upperFrame, text="HELP", width=4, height=1)
HelpButton.grid(row=0, column=4, padx=5, pady=5)





# INSIDE THE LEFT UPPER FRAME leftFrameUpper
# GENERATE RANDOM PASSWORD

ChooseRandom = Radiobutton(leftFrameUpper, text="Generate random password", variable=MainMenu, value=1)
ChooseRandom.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=4)

EmptyField1 = Label(leftFrameUpper, text="", width=10)
EmptyField1.grid(column=0, row=1)

LabelEnterLength = Label(leftFrameUpper, text="Enter length: ")
LabelEnterLength.grid(row=1, column=1, sticky=W)

FieldEnterLength = Text(leftFrameUpper, height=1, width = 3)
FieldEnterLength.grid(row=1, column=2, padx=2, pady=2)

EnterLengthOKButton = Button(leftFrameUpper, text="OK", height=1, width = 4)
EnterLengthOKButton.grid(row=1, column=3, padx=2, pady=2, sticky=W)

LabelUserEnteredLength = LabelUserEnteredLength = Label(leftFrameUpper, text='12', fg='grey')
LabelUserEnteredLength.grid(row=1, column=4, padx=2, pady=2, sticky=W)

LabelChooseStrength = LabelUserEnteredLength = Label(leftFrameUpper, text='Choose strength:')
LabelChooseStrength.grid(row=2, column=1, padx=2, pady=2, sticky=W)

ChooseStrength = IntVar()

strengthMODES = [
    (1, "Weak"),
    (2, "Medium"),
    (3, "Strong")
]
i = 3
for sValue, description in strengthMODES:
    rb = Radiobutton(leftFrameUpper, text=description, variable=ChooseStrength, value=sValue)
    rb.grid(row=i, column=1, sticky=W, columnspan=4)
    i += 1

# INSIDE THE LEFT LOWER FRAME leftFrameLower
# GENERATE PASSWORD WITH WORD SEQUENCE
ChooseWordSequence = Radiobutton(leftFrameLower, text="Word sequence-based password", variable=MainMenu, value=2)
ChooseWordSequence.grid(row=0, column=0, padx=5, pady=5, columnspan = 4, sticky=W)

LabelEnterWordSequence = Label(leftFrameLower, text="Enter words separated by spaces: ")
LabelEnterWordSequence.grid(row=1, column=0, columnspan = 3, sticky=W)

EmptyField2 = Label(leftFrameLower, text="", width=5)
EmptyField2.grid(column=0)

FieldEnterSequence = Text(leftFrameLower, height=1, width = 28)
FieldEnterSequence.grid(row=2, column=1)

EnterSequenceOKButton = Button(leftFrameLower, text="OK", height=1, width = 4)
EnterSequenceOKButton.grid(row=2, column=2, padx=2, pady=2, sticky=W)

LabelUserEnteredSequence = Label(leftFrameLower, text='cat wants food', fg='grey')
LabelUserEnteredSequence.grid(row=4, column=1, padx=2, pady=2, sticky=W)

LabelMenuSequence = Label(leftFrameLower, text='Use:')
LabelMenuSequence.grid(row=5, column=1, padx=2, pady=2, sticky=W)


seqCHOICES = [
    ("numseq", "numbers"),
    ("specseq", "special characters"),
    ("mixseq", "mixed case")
]

i=6
for variableName, description in seqCHOICES:
    variableName = IntVar()
    cb = Checkbutton(leftFrameLower, text=description, variable=variableName)
    cb.grid(row=i, column=1, sticky=W, columnspan=4)
    i += 1


# INSIDE THE RIGHT FRAME rightFrame
# CUSTOM WORD
ChooseCustomWord = Radiobutton(rightFrame, text="\"Crazy word\" password: \nenter your word and change it!", variable=MainMenu, value=3)
ChooseCustomWord.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=4)

customWordMODES = [
    (1, "Mix case randomly"),
    (2, "Change all the letters to look-alike\nnumbers and special characters"),
    (3, """Mix case and change a chosen number
        of letters to special characters and/or numbers"""),
    (4, """Add a chosen number of special characters and/or
     numbers in between the word's letters""")

]

customWordChoice = IntVar()
customWordChoice.set(1)

i = 3
for mode, description in customWordMODES:
    if mode == 4:
        i = 10
        r = Radiobutton(rightFrame, text=description, variable=customWordChoice, value=mode)
        r.grid(row=i, column=1, padx=2, pady=2, sticky=W, columnspan=4)
    elif mode in range(1,4):
        r = Radiobutton(rightFrame, text=description, variable=customWordChoice, value=mode)
        r.grid(row=i, column=1, padx=2, pady=2, sticky=W, columnspan=4)
        i += 1

LabelEnterHowMany_mixChange = Label(rightFrame, text="Enter how many new characters you want to add: ")
LabelEnterHowMany_mixChange.grid(row=11, column=2, sticky=W)

FieldEnterHowMany_mixChange  = Text(rightFrame, height=1, width = 3)
FieldEnterHowMany_mixChange.grid(row=11, column=3, padx=2, pady=2)

EnterHowManyOKButton_mixChange  = Button(rightFrame, text="OK", height=1, width = 4)
EnterHowManyOKButton_mixChange.grid(row=11, column=4, padx=2, pady=2, sticky=W)

LabelUserEnteredHowMany_mixChange  = LabelUserEnteredLength = Label(rightFrame, text='3', fg='grey')
LabelUserEnteredHowMany_mixChange.grid(row=11, column=5, padx=2, pady=2, sticky=W)


mixAndChangeWordCHOICES = [
    ("numword", "numbers"),
    ("specword", "special characters"),
    ("mixword", "mixed case")
]

i=12
for variableName, description in mixAndChangeWordCHOICES:
    variableName = IntVar()
    cb = Checkbutton(rightFrame, text=description, variable=variableName)
    cb.grid(row=i, column=2, sticky=W)
    i += 1

LabelEnterHowMany_addSpecials = Label(rightFrame, text="Enter how many letters you want to\n have changed to \"look-alikes\": ")
LabelEnterHowMany_addSpecials.grid(row=6, column=2, sticky=W)

FieldEnterHowMany_addSpecials = Text(rightFrame, height=1, width = 3)
FieldEnterHowMany_addSpecials.grid(row=6, column=3, padx=2, pady=2)

EnterHowManyOKButton_addSpecials = Button(rightFrame, text="OK", height=1, width = 4)
EnterHowManyOKButton_addSpecials.grid(row=6, column=4, padx=2, pady=2, sticky=W)

LabelUserEnteredHowMany_addSpecials = LabelUserEnteredLength = Label(rightFrame, text='2', fg='grey')
LabelUserEnteredHowMany_addSpecials.grid(row=6, column=5, padx=2, pady=2, sticky=W)


addSpecialsCHOICES = [
    ("numseq", "numbers"),
    ("specseq", "special characters"),
    ("mixseq", "mixed case")
]

i=6
for variableName, description in addSpecialsCHOICES:
    variableName = IntVar()
    cb = Checkbutton(leftFrameLower, text=description, variable=variableName)
    cb.grid(row=i, column=1, sticky=W, columnspan=4)
    i += 1

# INSIDE THE LOWER FRAME lowerFrame
# credits
a = Label(lowerFrame, text="Author: M.E. \nAll rights reserverd. \nSuggestions? Contact me(hyperlink)")
a.pack()

root.mainloop()
