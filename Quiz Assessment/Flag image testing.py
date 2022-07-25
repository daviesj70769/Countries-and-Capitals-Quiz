from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import re

root = Tk()

photo = PhotoImage(file="flag_img.png")
label = Label(root, image=photo)
label.pack()

root(mainloop)
        



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz")
    root.mainloop()