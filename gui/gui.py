from tkinter import *

root = Tk()
root.title('My Ultimate Password Generator')

# important variables
# MAIN MENU GROUP
MainMenu = IntVar()
ChooseStrength = IntVar()

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
Logo = Label(upperFrame, text="LOGO", height = 6, width = 10, relief=RIDGE)
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

EmptyField1 = Label(leftFrameUpper, text="", width=5)
EmptyField1.grid(column=0)

LabelEnterLength = Label(leftFrameUpper, text="Enter length: ")
LabelEnterLength.grid(row=1, column=1, sticky=W)

FieldEnterLength = Text(leftFrameUpper, height=1, width = 3)
FieldEnterLength.grid(row=1, column=2, padx=2, pady=2)

EnterLengthOKButton = Button(leftFrameUpper, text="OK", height=1, width = 4)
EnterLengthOKButton.grid(row=1, column=3, padx=2, pady=2, sticky=W)

LabelUserEnteredLength = Label(leftFrameUpper, text='12', fg='grey')
LabelUserEnteredLength.grid(row=1, column=4, padx=2, pady=2, sticky=W)



ChooseWeak = Radiobutton(leftFrameUpper, text="Weak", variable=ChooseStrength, value=1)
ChooseMedium = Radiobutton(leftFrameUpper, text="Medium", variable=ChooseStrength, value=2)
ChooseStrong = Radiobutton(leftFrameUpper, text="Strong", variable=ChooseStrength, value=3)

ChooseWeak.grid(row=2, column=1, sticky=W, columnspan=4)
ChooseMedium.grid(row=3, column=1, sticky=W, columnspan=4)
ChooseStrong.grid(row=4, column=1, sticky=W, columnspan=4)





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


# INSIDE THE RIGHT FRAME rightFrame
# CUSTOM WORD
ChooseCustomWord = Radiobutton(rightFrame, text="\"Crazy word\" password: \nenter your word and change it!", variable=MainMenu, value=3)
ChooseCustomWord.grid(row=0, column=0, padx=5, pady=5, sticky=W)




# INSIDE THE LOWER FRAME lowerFrame
# credits
a = Label(lowerFrame, text="Author: M.E. \nAll rights reserverd. \nSuggestions? Contact me(hyperlink)")
a.pack()

root.mainloop()
