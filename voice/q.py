import tkinter as tk
from tkinter import *

def printf(string):
    root = tk.Tk()
    w = tk.Label(root, text=string)
    w.pack()
    root.mainloop()


