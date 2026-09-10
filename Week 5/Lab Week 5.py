# Loops - information that needs to be repeated
# Types of loops

# While - depends on condition; condition stays true, loop continues
# For - sequences or number of iterations known

# continue - skips the remaining steps of current iteration and moves to the next one
# break - allows us to come out of the loop

# counter
# accumulator

# input validation with loops

# while - initial counter-value, condition, accumulator value to add into counter

# counter: int = 0
#
# while counter < 10:
#     print(counter, "Hello")
#     counter += 1

# for loop - range()
# for (int counter = 0; counter < 10; counter ++)


# print(list (range(10))) # start = 0, stop = 10, inc/dec = +1
# print(list (range (1,10,))) # start = 1, stop = 10, inc/dc = +1
# print(list range(1,10,2)) # start = 1, stop = 10, inc/dec = +2

# start from 10 and print till 1
# range (10, 1, -1)

# for counter in range(10):
#     print(counter, "Hello")

# problem - input as grade - check valid input - check in range 0 to 100 and print grade

# while True:
#     input_grade: str = input("Enter your grade: ")
#
#     if input_grade.replace(".", "", 1).isnumeric():
#         grade: float = float(input_grade)
#         if 0 <= grade <= 100:
#             print(grade)
#         else
#             print("out of range")
#     else:
#         print("Wrong input, try again")

# for - range(1,6) - 1, 2, 3, 4, 5
# grade 1 - 66 - valid input - range of 0 to 100 - okay
# grade 2 - 12345 - valid input - not in range - grade 2 or grade 3

# while counter, condition, valid input - valid range - total - increment counter

# counter: int = 1
# total: float = 0
#
# while counter < 6:
#     input_grade: str = input("Enter your grade: ")
#
#     if input_grade.replace(".", "", 1).isnumeric():
#         grade: float = float(input_grade)
#         if 0 <= grade <= 100:
#             print(grade)
#         else
#             print("out of range")
#     else:
#         print("Wrong input, try again")

# tkinter

import tkinter as tk
def submit_command():
    name = name_entry.get()
    age = age_entry.get()()

    result_label.config(text= f"My name is {name} and my age is {age}")

# problem - ask name and age input and print both name and age..
# window
root = tk.Tk()
root.geometry("500x400")
root.title("My First GUI")
#label
name_label = tk.Label(root, text= "Enter your name: ")
age_label = tk.Label(root, text= "Enter your age: ")
result_label = tk.Label(root, text="")

# entry
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

# button
submit_button = tk.Button(root, text = "Submit")
# pack
# name_label.pack()
# name_entry.pack()
# age_label.pack()
# age_entry.pack()
# root.mainloop()

# grid
name_label.grid(row = 0, column=0, padx=20, pady=20)
name_entry.grid(row = 0, column=1, padx=20, pady=20)

age_label.grid(row = 1, column=0, padx=20, pady=20)
age_entry.grid(row = 1, column=1, padx=20, pady=20)

submit_button.grid(row=2, columnspan=2)
result_label.grid(row=3, columnspan=2)
root.mainloop()