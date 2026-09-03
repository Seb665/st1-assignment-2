# AI Usage
# Part C - AI as tutor
#AI used - Microsoft Copilot

# Prompt Used:
# Act as a Python tutor. I am learning introductory software technology. Here is a small appointment booking function. task1enhanced
# Use lists, dictionaries and functions to enhance the Python file
#
# appointments = []
#
#
# def book_appointment(patient_name, practitioner_name, appointment_time):
#     if not patient_name:
#         raise ValueError("Patient name cannot be empty")
#
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#
#     appointments.append(appointment)
#
#
# def display_appointments():
#     if not appointments:
#         print("No appointments recorded.")
#         return
#
#     for appointment in appointments:
#         print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")
#
#
# print("Welcome to SmartCare: The Clinical Appointment Booking System!")
#
# book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
# book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
#
# display_appointments()
#
#
# 1. Explain what the code does.
# 2. Identify three limitations.
# 3. Suggest improvements.
# 4. Do not rewrite the whole application.
# 5. Ask me two questions to test my understanding.

# What I learned:
# I learnt that using dictionaries in a situation such as appointment booking is superior to using a simple list.
# Dictionaries are specifically good for data retrieval through key-value pairs. Thus, they are crucial in writing
# a program that satisfies the needs of the smartcare appointment system.

# Part D - AI alternative

# Prompt used:

# AI Generated alternative:

# List to store all appointments
appointments = []

# Function to add an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

# Add some appointments
book_appointment("Alice Smith", "Dr Brown", "10:00 AM")
book_appointment("Bob Johnson", "Dr Green", "11:30 AM")

# Display all appointments
for appointment in appointments:
    print("Patient:", appointment["patient"])
    print("Practitioner:", appointment["practitioner"])
    print("Time:", appointment["time"])
    print()

