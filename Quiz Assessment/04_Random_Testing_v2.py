# import random
# import csv
#
# with open('country_capitals_csv.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#
#     print(data)

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import csv
import random


class Start:
    def __init__(self, parent):
        # GUI for Quiz
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Quiz Heading
        self.country_capitals_label = Label(self.start_frame, text="Country and Capital's",
                                            font="Arial 19 bold")
        self.country_capitals_label.grid(row=0)

        # Answer Entry Box (row 3)
        self.answer_box = Entry(self.start_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.answer_box.grid(row=4, pady=10)

        # Capital Question



        # Country Answers

    with open("country_capitals_csv.csv", "r") as country_capitals_csv_file:
        csv_reader = csv.reader(country_capitals_csv_file)

        country_capital_names = list(csv_reader)[1:]
        random.shuffle(country_capital_names)

        # choose random item from a list
        random_q_a = random.choice(country_capital_names)

        question = random_q_a[1]
        print(question)
        answer = random_q_a[0]
        print(answer)

        print(random_q_a)

        print("Can you figure out what country it is based on the capital?")



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country and capitals quiz")
    Start(root)
    root.mainloop()

