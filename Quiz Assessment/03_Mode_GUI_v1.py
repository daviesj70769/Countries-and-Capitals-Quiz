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
        self.Quiz_box_label.grid(row=1)

        # Play button goes here (row 3)
        self.play_button = Button(self.start_frame, text="Play",
                                  bg="midnight blue", fg="white", font="Arial 15 bold", width=20,
                                padx=10, pady=10, command=self.mode)
        self.play_button.grid(row=4, pady = 10)
    
    def mode(self):
        print("Choose a mode!")
        choose_mode = Mode(self)
        choose_mode.mode_text.configure
    
class Mode:
    def __init__(self, partner):

        # GUI Setup/Frame
        self.mode_box = Toplevel()

        self.mode_frame = Frame(self.mode_box)
        self.mode_frame.grid()
       
        # Heading row 
        self.heading_label = Label(self.mode_box, text="Choose a mode",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Easy Button
        self.easy_Button = Button(self.mode_frame, text="Easy",
                                  bg="orange", fg="White", font="arial 12 bold",
                                  padx=10, pady=10, command=self.mode)
        self.easy_Button.grid(row=4, pady=10)

        # Instructions label
        self.mode_text = Label(self.mode_box, wrap=300, justify=LEFT,
                                        text="When Choosing a mode note that there is 3 different Modes.\n\nThe first mode is Easy which is 10 Questions.\n\nThe second mode is Medium which is 20 Questions.\n\nThe Third mode is Hard which is 30 Questions.\n\n",
                                        font="Arial 10", padx=10, pady=10)
        self.mode_text.grid(row=3)

class Easy:
    def __init__(self,partner):

        # # If users press cross at top, game quits
        # self.mode_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # # Quit Button
        # self.quit_button = Button(self.mode_frame, text="Quit", fg="white",
        #                           bg="#660000", font="Arial 15 bold", width=20,
        #                           command=self.to_quit, padx=10, pady=10)
        # self.quit_button.grid(row=6, pady=10)
        
        


# main routine
        if __name__ == "__main__":
            root = Tk()
            root.title("Mystery Box")
            Start(root)
            root.mainloop()