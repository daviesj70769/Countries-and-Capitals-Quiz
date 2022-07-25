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

       # Help and Play button (row 3)
        self.help_export_frame = Frame(self.start_frame)
        self.help_export_frame.grid(row=2, pady=10, padx=10)
       
        self.play_button = Button(self.help_export_frame, text="Play",
                                  bg="midnight blue", fg="white", font="Arial 15 bold") 
        self.play_button.grid(row=0, column =0, padx=10, pady = 10)

        self.help_button = Button(self.help_export_frame, text="Help",
                                  font="Arial 15 bold",
                                  bg="maroon", fg="white", command=self.help)
        self.help_button.grid(row=0, column=1, padx=2)

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure
        
class Help:
    def __init__(self, partner):

        button_font = "Arial 12 bold"
        
        # disable help button
        partner.help_button.config(state=DISABLED)
        
        #sets up child window (ie: help box)
        self.help_box = Toplevel()        
       
        # If user press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
       
        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300,)
        self.help_frame.grid()
       
        # Set up Help Heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                font =button_font)
        self.how_heading.grid(row=0)                        
        
        help_text="Hi, :)"

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row = 1)
        
        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", 
                                  width=10, 
                           command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, padx=10, pady=10)                   
        
    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



    
    
# main routine
if __name__ == "__main__":
        root = Tk()
        root.title("Flag Quiz")
        Start(root)
        root.mainloop()