import tkinter as tk

master_window = tk.Tk()
master_window.geometry("150x150")
master_window.title("StringVar Example")

string_variable = tk.StringVar(master_window, "Hello Everyone!!")

label = tk.Label(master_window, textvariable=string_variable, height=150)
label.pack()

master_window.mainloop()

string_variable = tk.StringVar(master=master_window, value="Initial value of string variable")

string_variable = tk.StringVar(master_window)
string_variable.set("Some Text")