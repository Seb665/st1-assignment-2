# data types: list, tuple, dictionary
# for each loop
# 2D list
# file handling
# exception handling
# matplotlib

# data types: str, float, int, bool -> immutable

# list vs arrays

# arr [5] = [1,2,3,4,5]
# list = []
# index starts from 0

# students: list = ["Alice", "Bob", "David", "John", "Emma"]
#
# # print(students[1])
# # students.append("Emily")
# # students.insert(1, "Emma")
# # students.pop() # removes the last item in a list
# # students.remove("Bob")
# # students.extend(["Tom", "Jane"])
# #
# # print(students)
#
# for count in range(len(students)): # [0,1,2,3,4]
#     print(count, students[count])
#
# # for each loop
# # enumerate -> [index, students[index]]
# for student in enumerate(students, start= 1):
#     print(index, student)

# students: list[str | bool | int | list] = ["Alice", "Bob", True, 22, []]

# from copy import deepcopy
# lyst1 = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# # print(lyst1[1][1])
# lyst2 = deepcopy(lyst1)
#
# print(f"{lyst1 = }")
# print(f"{lyst2 = }")
#
# lyst2[1][1] = 0
# print()
# print(f"{lyst1 = }")
# print(f"{lyst2 = }")


# tuple

# students: tuple[str | int, ...] = ("John", "Bob", "David", "Emma", 1)
#
# print(students[1])
#
# def enumerate_test():
#     return 1,2
#
# print(enumerate_test())


# dictionary
# key-value pair
# each key is unique


# student: dict[str, str | int] = {"name": "David", "age": 25, "unit": "ST1", "name": "John"}
#
# print(student["name"])
# # print(student["course"]) # safe to access value
# print(student.get("name", "Key does not exist")) # safe to access dictionary
#
# student["course"] = "Engineering"
# print(student)
#
# print(student.items())
# print(student.keys())
# print(student.values())
#
# # for each loop
# for key, value in student.items():
#     print(key, value)

# student: dict[str, str | int] = {"name": "David", "age": 25, "unit": "ST1"}
#
# # list[dict]
#
# # 0(n^2)
# studnets: list[dict] = [
#     {"name": "David", "age": 25, "unit": "ST1"}
#     {"name": "John", "age": 20, "unit": "ST1"}
#     {"name": "Emma", "age": 29, "unit": "ST1"}
# ]
#
# # 0(1)
# students_dict: dict[dict] = {
#     3238081: {"name": "David", "age": 25, "unit": "ST1"},
#     3238082: {"name": "John", "age": 20, "unit": "ST1"},
#     3238083: {"name": "Emma", "age": 29, "unit": "ST1"},
# }


# file handling -> read(r), write(w), append(a)
# use write(w) to create the file
# with write(w) overrides the new data
# use append mode
# open -> do something -> close

# file = open("students.txt", "w")
#
# file.write("Emily\n")
#
# file.close()

# try:
#     file = open("students.txt", "r")
#
#     for line in file:
#         print(line.strip()) # Pranav's suggested method
#
#     print(2/0)
# except FileNotFoundError:
#     print("File does not exist")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception as e:
#     print({type(e).__name__})
# finally:
#     print("file closed")
#     file.close()

# pip install matplotlib
# pip3 install matplotlib

import matplotlib.pyplot as plt

students: list = ["Alice", "Bob", "John", "Emma"]
grades: list = [45, 22, 67, 89]

plt.plot(students, grades)

plt.title("Grade foro students")
plt.xlabel("Student")
plt.ylabel("Grade")

plt.show()