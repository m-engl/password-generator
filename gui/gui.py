from tkinter import *

root = Tk()
root.title('My Ultimate Password Generator')

upperFrame = Frame(root, height=100, width=630, padx=3, pady=3, highlightbackground="black", highlightthickness=1).grid(row=0, column=0, columnspan=2)
upperLeftFrame = Frame(root, height=200, width=270, padx=3, pady=3, borderwidth=10, highlightbackground="black", highlightthickness=1).grid(row=1, column=0)
lowerLeftFrame = Frame(root, height=250, width=270, padx=3, pady=3, highlightbackground="black", highlightthickness=1).grid(row=2, column=0)
rightFrame = Frame(root, height=450, width=360, padx=3, pady=3, highlightbackground="black", highlightthickness=1).grid(row=1, column=1, rowspan = 2)
lowerFrame = Frame(root, height=40, width=630, padx=3, pady=3, highlightbackground="black", highlightthickness=1).grid(row=3, column=0, columnspan=2)

root.mainloop()
