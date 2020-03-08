from tkinter import *

root = Tk()
root.title('My Ultimate Password Generator')

# important variables
# MAIN MENU GROUP
MainMenu = IntVar()


# CREATE FRAMES
upperFrame = Frame(root, height=100, width=630, highlightbackground="black", highlightthickness=1) #
leftFrameUpper = Frame(root, height=200, width=270, highlightbackground="black", highlightthickness=1) #
leftFrameLower = Frame(root, height=250, width=270, highlightbackground="black", highlightthickness=1) #
rightFrame = Frame(root, height=450, width=360, highlightbackground="black", highlightthickness=1) #
lowerFrame = Frame(root, height=40, width=630, highlightbackground="black", highlightthickness=1) # ,

# PLACE FRAMES
upperFrame.grid(row=0, column=0, columnspan=2, sticky='WESN')
# upperFrame.grid_propagate(False) # used to never resize the frame
leftFrameUpper.grid(row=1, column=0, sticky='NSEW')
leftFrameLower.grid(row=2, column=0, sticky='NSEW')
rightFrame.grid(row=1, column=1, rowspan = 2, sticky='NSEW')
lowerFrame.grid(row=3, column=0, columnspan=2, sticky='WESN')

# INSIDE THE UPPER FRAME upperFrame


logo = PhotoImage(file="logo.gif")
Logo = Label(upperFrame, image=logo)
Logo.grid(row=0, column=0, rowspan=3, padx=10, pady=5)

TextBegin = Label(upperFrame, text="Before generating the password, choose your options below.")
TextBegin.grid(row=4, column=0, columnspan=5, padx=10, pady=5, sticky=W)

GenPassButton = Button(upperFrame, text="Generate\nPassword")
GenPassButton.grid(row=1, column=1, padx=5, pady=5)

YourNewPasswordIs = Label(upperFrame, text="Your new password is:")
YourNewPasswordIs.grid(row=0, column=2, padx=5, pady=1, sticky=W)

ThePassword = Text(upperFrame, height=1, width = 35, bg="light goldenrod")  # , relief="solid", borderwidth=1
ThePassword.grid(row=1, column=2)

CopyButton = Button(upperFrame, text="Copy")
CopyButton.grid(row=2, column=2, padx=5, pady=1)





# INSIDE THE LEFT UPPER FRAME leftFrameUpper
# GENERATE RANDOM PASSWORD

ChooseRandom = Radiobutton(leftFrameUpper, text="Generate random password", variable=MainMenu, value=1)
ChooseRandom.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=4)

# EmptyField1 = Label(leftFrameUpper, text="", width=10)
# EmptyField1.grid(column=0, row=1)

LabelEnterLength = Label(leftFrameUpper, text="Enter length: ")
LabelEnterLength.grid(row=1, column=1, padx=(20, 5), pady=5, sticky=W)

FieldEnterLength = Text(leftFrameUpper, height=1, width = 3, bg="snow2")  # , relief="solid", borderwidth=1
FieldEnterLength.grid(row=1, column=2, padx=2, pady=2)

EnterLengthOKButton = Button(leftFrameUpper, text="OK", height=1, width = 4)
EnterLengthOKButton.grid(row=1, column=3, padx=2, pady=2, sticky=W)

LabelUserEnteredLength = LabelUserEnteredLength = Label(leftFrameUpper, text='12', fg='grey')
LabelUserEnteredLength.grid(row=1, column=4, padx=2, pady=2, sticky=W)

LabelChooseStrength = Label(leftFrameUpper, text='Choose strength:')
LabelChooseStrength.grid(row=2, column=1, padx=(25, 5), pady=2, sticky=W)

ChooseStrength = IntVar()

strengthMODES = [
    (1, "Weak"),
    (2, "Medium"),
    (3, "Strong")
]
i = 3
for sValue, description in strengthMODES:
    rb = Radiobutton(leftFrameUpper, text=description, variable=ChooseStrength, value=sValue)
    rb.grid(row=i, column=1, sticky=W, padx=(25, 5), columnspan=4)
    i += 1

# INSIDE THE LEFT LOWER FRAME leftFrameLower
# GENERATE PASSWORD WITH WORD SEQUENCE
ChooseWordSequence = Radiobutton(leftFrameLower, text="Word sequence-based password", variable=MainMenu, value=2)
ChooseWordSequence.grid(row=0, column=0, padx=5, pady=5, columnspan = 3, sticky=W)

LabelEnterWordSequence = Label(leftFrameLower, text="Enter words separated by spaces: ")
LabelEnterWordSequence.grid(row=1, column=0, columnspan=3, sticky=W, padx=(20, 5), pady=(5))

FieldEnterSequence = Text(leftFrameLower, height=1, width = 28, bg="snow2")  # , relief="solid", borderwidth=1
FieldEnterSequence.grid(row=2, column=0, padx=(20, 5), columnspan=3)

EnterSequenceOKButton = Button(leftFrameLower, text="OK", height=1, width = 4)
EnterSequenceOKButton.grid(row=3, column=1, padx=(20, 30), sticky=W, columnspan=3)

LabelUserEnteredSequence = Label(leftFrameLower, text='cat wants food', fg='grey')
LabelUserEnteredSequence.grid(row=3, column=2, padx=2, pady=2, sticky=W)

LabelMenuSequence = Label(leftFrameLower, text='Use:')
LabelMenuSequence.grid(row=5, column=1, padx=(25, 5), pady=(5), sticky=W)


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
ChooseCustomWord = Radiobutton(rightFrame, text="\"Crazy word\" password", variable=MainMenu, value=3, justify="left")
ChooseCustomWord.grid(row=0, column=0,  padx=(0, 5), sticky=W, columnspan=3)

# CUSTOM WORD ENTER and confirm

LabelEnterWord = Label(rightFrame, text="Enter your word:")
LabelEnterWord.grid(row=1, column=0, sticky=W, padx=(20, 5), pady=(5))

FieldEnterWord = Text(rightFrame, height=1, width = 15, bg="snow2")  # , relief="solid", borderwidth=1
FieldEnterWord.grid(row=1, column=1, padx=(5, 2), columnspan=2, sticky=W)

EnterWordOKButton = Button(rightFrame, text="OK", height=1, width = 4)
EnterWordOKButton.grid(row=1, column=3, padx=(2,2), sticky=W)

LabelUserEnteredWord = Label(rightFrame, text='peculiar', fg='grey')
LabelUserEnteredWord.grid(row=2, column=1, padx=2, pady=2, sticky=W)

LabelMenuWord = Label(rightFrame, text='Choose your options:')
LabelMenuWord.grid(row=3, column=0, padx=(25, 5), pady=(5), sticky=W)





customWordMODES = [
    (1, "Mix case randomly"),
    (2, "Change all the letters to look-alike\nnumbers and special characters"),
    (3, "Mix case and change a chosen number \nof letters to special characters and/or numbers"),
    (4, "Add a chosen number of special characters and/or\nnumbers in between the word's letters")

]

customWordChoice = IntVar()
customWordChoice.set(1)

def create_radio_for_customWord():
    r = Radiobutton(rightFrame, text=description, variable=customWordChoice, value=mode, justify="left")
    r.grid(row=i, column=0, padx=(25, 25), pady=2, sticky=W, columnspan=3)
    return r

i = 4
for mode, description in customWordMODES:
    if mode == 4:
        i = 11
        create_radio_for_customWord()

    elif mode in range(1,4):
        create_radio_for_customWord()
        i += 1

# mix and change

LabelEnterHowMany_mixChange = Label(rightFrame, text="Enter how many letters you want\nto have changed to \"look-alikes\": ", justify="left")
LabelEnterHowMany_mixChange.grid(row=7, column=0, padx=(45,5), sticky=W, columnspan=2)

FieldEnterHowMany_mixChange = Text(rightFrame, height=1, width = 3, bg="snow2")  # , relief="solid", borderwidth=1
FieldEnterHowMany_mixChange.grid(row=7, column=1, padx=5, pady=2)

EnterHowManyOKButton_mixChange = Button(rightFrame, text="OK", height=1, width = 4)
EnterHowManyOKButton_mixChange.grid(row=7, column=2, padx=2, pady=2, sticky=W)

LabelUserEnteredHowMany_mixChange = Label(rightFrame, text='2', fg='grey')
LabelUserEnteredHowMany_mixChange.grid(row=7, column=3, padx=2, pady=2, sticky=W)


# add specials with option choice

LabelEnterHowMany_addSpecials = Label(rightFrame, text="Enter how many new\ncharacters you want to add: ", justify="left")
LabelEnterHowMany_addSpecials.grid(row=12, column=0, padx=(45, 5), sticky=W, columnspan=2)

FieldEnterHowMany_addSpecials  = Text(rightFrame, height=1, width = 3, bg="snow2")  # , relief="solid", borderwidth=1
FieldEnterHowMany_addSpecials.grid(row=12, column=1, padx=2, pady=2)

EnterHowManyOKButton_addSpecials  = Button(rightFrame, text="OK", height=1, width = 4)
EnterHowManyOKButton_addSpecials.grid(row=12, column=2, padx=2, pady=2, sticky=W)

LabelUserEnteredHowMany_addSpecials  = Label(rightFrame, text='3', fg='grey')
LabelUserEnteredHowMany_addSpecials.grid(row=12, column=3, padx=2, pady=2, sticky=W)

LabelUse = Label(rightFrame, text='Use:')
LabelUse.grid(row=13, column=0, padx=55, pady=2, sticky=W)

addSpecialsCHOICES = [
    ("numseq", "numbers"),
    ("specseq", "special characters"),
    ("mixseq", "mixed case")
]

i=14
for variableName, description in addSpecialsCHOICES:
    variableName = IntVar()
    cb = Checkbutton(rightFrame, text=description, variable=variableName, anchor=W)
    cb.grid(row=i, column=0, sticky=W, padx=(60))
    i += 1

# INSIDE THE LOWER FRAME lowerFrame
# credits
a = Label(lowerFrame, text="Author: M.E. \nAll rights reserverd. \nSuggestions? Contact me(hyperlink)")
a.grid(column=0, row=0, padx=80, pady=5)

HelpButton = Button(lowerFrame, text="HELP", width=4, height=1)
HelpButton.grid(column=1, row=0, sticky=E, padx=(60,5))

root.mainloop()
