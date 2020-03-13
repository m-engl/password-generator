import tkinter as tk

class Upper_Frame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.Logo = tk.Label(self, image=master.logo)
        self.Logo.grid(row=0, column=0, rowspan=3,
                       padx=5, pady=5)

        self.TextBegin = tk.Label(self, text="Before generating the password, choose your options below.")
        self.TextBegin.grid(row=4, column=0, columnspan=5,
                            padx=10, pady=2,
                            sticky='W')

        self.GenPassButton = tk.Button(self, text="Generate",
                                       width = 12, height=2,
                                       command=self.master.display_password)
        self.GenPassButton.grid(row=2, column=1, rowspan=2,
                                padx=5, pady=5)

        self.YourNewPasswordIs = tk.Label(self, text="Your new password is:")
        self.YourNewPasswordIs.grid(row=1, column=2,
                                    padx=5, pady=(5,1),
                                    sticky='S')

        self.ThePassword = tk.Entry(self, width=35, textvariable=self.master.password,
                                    bg="light goldenrod")  # , relief="solid", borderwidth=1
        self.ThePassword.grid(row=2, column=2, rowspan=2)

        self.CopyButton = tk.Button(self, text="Copy")
        self.CopyButton.grid(row=2, column=3, rowspan=2,
                             padx=5, pady=1)