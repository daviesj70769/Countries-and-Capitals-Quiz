from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import re

class Start:
    def __init__(self, parent):

        # GUI for Flag Quiz
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Quiz Heading 
        self.Quiz_box_label = Label(self.start_frame, text="Flag Quiz",
                                    font="Arial 19 bold")
        self.Quiz_box_label.grid(row=0, column=0)

        # Quiz text
        self.start_text = Label(self.start_frame, text="Welcome to my Flag Quiz "
                                                       "i have got a large variety of "
                                                       "flag questions and i hope you enjoy the quiz, "
                                                       "as it is my first ever peice of code that i have done "
                                                       "majority of by myself.\n\n"
                                                       "press play when ready!",
                                           justify=LEFT, width=40, wrap=250, font= "Arial 12")
        self.start_text.grid(row=1)

        # Play Button
        self.play_button = Button(self.start_frame, text="Play",
                                  bg="Midnight blue", fg="white",
                                  padx=10, pady=10, command=self.mode)
        self.play_button.grid(row=5, pady=10)

    def mode(self):
        print("Choose a mode")
        get_mode = Mode(self)
    #   get_mode.help_text_config

class Mode:
    def __init__(self, partner):
    
        # GUI Setup
        self.mode_box = Toplevel()

        self.mode_frame = Frame(self.mode_box, width=300)
        self.mode_frame.grid()
   
        # If user press cross at top, closes help and 'releases' help button
        self.mode_box.protocol('WM_DELETE_WINDOW', partial(self.to_quit, partner))

         # Set up Help Heading (row 0)
        self.how_heading = Label(self.mode_frame, text="Choose a mode",
                                 font="arial 18 bold")
        self.how_heading.grid(row=0)

    # def close_mode(self, partner):
    #     # Put help button back to normal...
    #     partner.mode_button.config(state=NORMAL)
    #     self.mode_frame.destroy()
    
    def to_quit(self):
        root.destroy()  


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz")
    Start(root)
    root.mainloop()