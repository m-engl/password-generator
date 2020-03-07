from tkinter import *

root = Tk()
root.title('My Ultimate Password Generator')

# CREATE FRAMES
upperFrame = Frame(root, height=100, width=630, highlightbackground="black", highlightthickness=1)
upperLeftFrame = Frame(root, height=200, width=270, highlightbackground="black", highlightthickness=1)
lowerLeftFrame = Frame(root, height=250, width=270, highlightbackground="black", highlightthickness=1)
rightFrame = Frame(root, height=450, width=360, highlightbackground="black", highlightthickness=1)
lowerFrame = Frame(root, height=40, width=630, highlightbackground="black", highlightthickness=1)

# PLACE FRAMES
upperFrame.grid(row=0, column=0, columnspan=2)
# upperFrame.grid_propagate(False) # used to never resize the frame
upperLeftFrame.grid(row=1, column=0)
lowerLeftFrame.grid(row=2, column=0)
rightFrame.grid(row=1, column=1, rowspan = 2)
lowerFrame.grid(row=3, column=0, columnspan=2)

# INSIDE THE UPPER FRAME

# LOGO - the label is the working version,
# later there is going to be an image
# about h=60 and w=120 px, right now it is text units as
# when stuff contain text, h and w are in text units
Logo = Label(upperFrame, text="LOGO", height = 6, width = 10, relief=RIDGE)
Logo.grid(row=0, column=0, rowspan=3)

TextBegin = Label(upperFrame, text="Before generating the password, choose your options below.")
TextBegin.grid(row=4, column=0, columnspan=5)

GenPassButton = Button(upperFrame, text="Generate\nPassword")
GenPassButton.grid(row=1, column=1)

YourNewPasswordIs = Label(upperFrame, text="Your new password is:")
YourNewPasswordIs.grid(row=0, column=2)

ThePassword = Text(upperFrame, height=1, width = 35)
ThePassword.grid(row=1, column=2)

CopyButton = Button(upperFrame, text="Copy")
CopyButton.grid(row=2, column=2)

HelpButton = Button(upperFrame, text="HELP", width=6, height=6)
HelpButton.grid(row=1, column=4, rowspan=2)




root.mainloop()
