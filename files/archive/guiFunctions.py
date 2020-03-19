import gui
import generator-classes as gc
import tkinter as tk

def deactivate_other_options(frame):
    for child in frame.winfo_children():
        child['state'] = 'disabled'

