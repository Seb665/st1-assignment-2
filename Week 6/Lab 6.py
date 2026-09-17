# functions
# void -> when called from a point it doesn't send any value back
# return -> when called from a point, it sends value back and we need to store it or print()
# type hints
# documentation
# input validation
# scope of variable
# modules
# move from top to bottom approach to functional programming

# recursion

# def welcome_screen():
#     print("Welcome to St1")
#     print("__" * 15)
#
# welcome_screen()

# return
# scopes -> global, local, parameter
# def add_number():
#     number1: int = 10
#     number2: int = 5
#     total: int = number1 + number2
#     return total
#
# add_number()

# recursion

# SOC = a class, a file, a function should have least amount of responsibility

# def main():
#     print(add_number(1, 2))
#
#
# if __name__ == '__main__':
#     main()

# import calculator as cl
#
# # from calculator import add_numbers, sub_numbers
# # from calculator import *
# print(cl.add_numbers(2, 2))

# def main():
#     while True:
#         input_grade: str = input("Enter your grade: ")
#         if input_grade.isnumeric():
#             grade: int = int(input_grade)
#             print(grade)
#             break
#         else:
#             print("Wrong input, try again")

# factorial
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 5! = return 5 * factorial(4)
# 4! = return 4 * factorial(3)
# 3! = return 3 * factorial(2)
# 2! = return 2 * factorial(1)
# 1! = return 1 * factorial(0)
# 0! = return 1


# def factorial(number: int) -> int:
#     if number == 0:
#         return 1
#     return number * factorial(number - 1)
#
# def main() -> None:
#     print(factorial(5))







