from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
# import csv
# import random
#
# with open("country_capitals_csv.csv", "r") as country_capitals_csv_file:
#     csv_reader = csv.reader(country_capitals_csv_file)
#
#     country_capital_names = list(csv_reader)[1:]
#     random.shuffle(country_capital_names)
#
#     data = list(csv.reader)
#     print(data)
#
#     # choose random item from a list
#     # random_q_a = random.choice(country_capital_names)

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
        self.country_capitals_label = Label(self.start_frame, text="Capitals and Countries",
                                            font="Arial 19")
        self.country_capitals_label.grid(row=0)

        # Answer Entry Box (row 3)
        self.answer_box = Entry(self.start_frame, width=20,
                                font="Arial 14 bold", justify=CENTER)
        self.answer_box.grid(row=4, pady=10)


        with open("country_capitals_csv.csv", "r") as country_capitals_csv_file:
            csv_reader = csv.reader(country_capitals_csv_file)

            country_capital_names = list(csv_reader)[1:]
            random.shuffle(country_capital_names)

            data = list(csv.reader)
            print(data)

                # # Capital Question
                # self.capital_question = Label(self.start_frame, text=(list[1]), font="Arial 15 bold ")
                # self.capital_question.grid(row=1)
                #
                # # Country Answers
                # self.country_answer1 = Label(self.start_frame, text=(list[0]), font="Arial 15 bold ")
                # self.country_answer1.grid(row=5)

            for country in range(5):
                print(country)
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals and Countries quiz")
    Start(root)
    root.mainloop()



