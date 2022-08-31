from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import re
import csv
from random import shuffle


class Start:
    def __init__(self, parent):

        self.var_countries = StringVar()
        self.my_score = IntVar()

        self.my_score.set(0)

        # set up variable to hold question

        # GUI for Quiz
        self.start_frame = Frame(padx=15, pady=15)
        self.start_frame.grid()

        # Quiz Heading
        self.country_capitals_label = Label(self.start_frame, text="Capitals and Countries",
                                            font="Arial 19")
        self.country_capitals_label.grid(row=0)

        # Initial Instructions (row 1)
        self.quiz_instructions = Label(self.start_frame, font="Arial 11 italic",
                                          text="Please press the <next> button",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Entry box (row 2)
        self.entry_frame = Frame(self.start_frame, width=200)
        self.entry_frame.grid(row=2)

        # Entry Box (row 3)
        self.entry_box = Entry(self.start_frame, width=20,
                                font="Arial 14 bold", justify=CENTER)
        self.entry_box.grid(row=3, pady=10)

        # amount_error label (set to blank at start)
        self.answer_label = Label(self.start_frame, font="Arial 10 italic",
                                  text="Answer goes here",
                                  wrap=275, justify=LEFT, padx=10, pady=10)
        self.answer_label.grid(row=4)

        # Check and Next button (row 5)
        self.quiz_export_frame = Frame(self.start_frame)
        self.quiz_export_frame.grid(row=5, pady=15, padx=15)

        # Check Button
        self.check_button = Button(self.quiz_export_frame, width = 15, text="Check",
                                   font="Arial 12 bold", bg = "Dark green", fg="white", command=self.check_answer)
        self.check_button.grid(row=5,column=0, padx=15, pady=15)

        # Next Button
        self.check_button = Button(self.quiz_export_frame, width=15, text="Next",
                                   font="Arial 12 bold", bg="black", fg="white", command=self.next_question)
        self.check_button.grid(row=5,column=1, padx=15, pady=15)

        # Quit Button
        self.quit_quiz_button = Button(self.quiz_export_frame,width=15, text="Quit",
                                      font="Arial 12 bold", bg="Grey", fg="white", command=self.to_quit)
        self.quit_quiz_button.grid(row=6, padx=15,columnspan=3, pady=15)

    def to_quit(self):
        root.destroy()

    def next_question(self):
        with open("country_capitals_csv.csv", "r") as country_capitals_csv_file:
            csv_reader = csv.reader(country_capitals_csv_file)

            country_list = list(csv_reader)[1:]

            # choose random item from a list
            random_q_a = random.choice(country_list)

            question = random_q_a[1]
            print(question)
            answer = random_q_a[0]
            print(answer)

            self.var_countries.set(answer)

            print("Type in the text box what country you think it is...")

            # clear entry box??
            self.entry_box.config(bg="white")
            self.entry_box.delete(0, END)

            self.quiz_instructions.config(text=question, font = "Arial 15 bold ")

            # Capital Question
            # self.capital_question = Label(self.start_frame, text=(random_q_a [1]), font = "Arial 15 bold ")
            # self.capital_question.grid(row=2)


            # # Country Answer
            # self.country_answer1 = Label(self.start_frame, text =(random_q_a [0]), font = "Arial 15 bold ")
            # self.country_answer1.grid(row=5)


    def check_answer(self):
        # Check answer - if what the user wrote is the same as what is in position 0 then it is correct but if it is,
        # not the same as position 0 it is incorrect.

        country_answer = self.var_countries.get()
        user_answer = self.entry_box.get()

        score = self.my_score.get()

        # print(user_answer)
        print(country_answer)

        error_back = "#ffafaf"
        correct_back = "Pale Green"

        if user_answer == country_answer:
            has_errors = "no"

            score += 1
            self.my_score.set(score)

            error_feedback =" That is correct!  Score: {}/10, press next to continue".format(score)

        else:
            has_errors = "yes"
            error_feedback ="You are wrong, the answer is {}".format(country_answer)

        if has_errors == "yes":
            self.entry_box.config(bg=error_back)
            self.answer_label.config(text=error_feedback, font="Arial 10 italic")

        if has_errors == "no":
            self.entry_box.config(bg=correct_back)
            self.answer_label.config(text=error_feedback, font="Arial 10 italic")










# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Capitals and Countries quiz")
    Start(root)
    root.mainloop()

