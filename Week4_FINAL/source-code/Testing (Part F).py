# ----- PART F: VERIFYING BEHAVIOUR -----

# TEST 1: TESTING NORMAL APPOINTMENT

# ----- VERIFYING NORMAL APPOINTMENT USING HUMAN CODE -----:

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
#
# display_appointments()

# Output displayed after running above code:
# Patient: Alice Smith | Practitioner: Dr. John Doe | Time: 2024-07-20 10:00 AM


# ----- VERIFYING NORMAL APPOINTMENT USING AI-GENERATED CODE -----:

# appointments = []
#
# # Function to add an appointment
# def book_appointment(patient_name, practitioner_name, appointment_time):
#
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#
#     appointments.append(appointment)
#
# # Add some appointments
# book_appointment("Alice Smith", "Dr Brown", "10:00 AM")
#
# # Display all appointments
# for appointment in appointments:
#     print("Patient:", appointment["patient"])
#     print("Practitioner:", appointment["practitioner"])
#     print("Time:", appointment["time"])
#     print()

# Output displayed after running the above code:
# Patient: Alice Smith
# Practitioner: Dr Brown
# Time: 10:00 AM

# TEST 2: TESTING BLANK PATIENT NAME

# ----- VERIFYING BLANK NAME USING HUMAN CODE -----:

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
# book_appointment('', 'Dr. John Doe', '2024-07-20 10:00 AM')
#
# display_appointments()

# Output displayed after running the code above:
# ValueError: Patient name cannot be empty

# ----- VERIFYING BLANK NAME USING AI-GENERATED CODE -----:

appointments = []

# Function to add an appointment
# def book_appointment(patient_name, practitioner_name, appointment_time):
#
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#
#     appointments.append(appointment)
#
# # Add some appointments
# book_appointment("", "Dr Brown", "10:00 AM")
#
# # Display all appointments
# for appointment in appointments:
#     print("Patient:", appointment["patient"])
#     print("Practitioner:", appointment["practitioner"])
#     print("Time:", appointment["time"])
#     print()
#
# # Output displayed after running the code above:
# # The program accepted and stored an appointment with a blank patient's name
#
# # ----- TEST 3: Same practitioner at the same time -----:
#
# ----- VERIFYING SAME PRACTITIONER AT THE SAME TIME USING THE HUMAN CODE -----:
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
# book_appointment('Bob Johnson', 'Dr. John Doe', '2024-07-20 11:30 AM')
#
# display_appointments()

# Output displayed after running the above code
# Both appointments were accepted even though they used the same practitioner and appointment time. Double bookings
# were not detected.

# ----- VERIYING SAME PRACTITIONER AT THE SAME TIME USING AI-GENERATED CODE -----:

# appointments = []
#
# # Function to add an appointment
# def book_appointment(patient_name, practitioner_name, appointment_time):
#
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#
#     appointments.append(appointment)
#
# # Add some appointments
# book_appointment("Alice Smith", "Dr Brown", "10:00 AM")
# book_appointment("Bob Johnson", "Dr Brown", "11:30 AM")
#
# # Display all appointments
# for appointment in appointments:
#     print("Patient:", appointment["patient"])
#     print("Practitioner:", appointment["practitioner"])
#     print("Time:", appointment["time"])
#     print()

# Output displayed after running the above code:
# Both appointments were accepted for the same practitioner and time. Double bookings were not detected.

# ----- TEST 4: patient_name=None -----:

# ----- VERIFYING THE INPUT patient_name=None USING THE HUMAN CODE-----:

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
# book_appointment(None, 'Dr. John Doe', '2024-07-20 10:00 AM')
#
# display_appointments()

# Output displayed after running the above code:
# None was rejected as the patient's name and a ValueError was displayed.

# ----- VERIFYING THE INPUT patient_name=None USING THE AI-GENERATED CODE -----:

# appointments = []
#
# # Function to add an appointment
# def book_appointment(patient_name, practitioner_name, appointment_time):
#
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#
#     appointments.append(appointment)
#
# # Add some appointments
# book_appointment(None, "Dr Brown", "10:00 AM")
#
# # Display all appointments
# for appointment in appointments:
#     print("Patient:", appointment["patient"])
#     print("Practitioner:", appointment["practitioner"])
#     print("Time:", appointment["time"])
#     print()

# Output displayed after running the above code:
# The program accepted None as the patient's name

# ----- TEST 5: appointment_time=None -----:

# ----- VERIFYING appointment_time=None FOR THE HUMAN CODE -----:

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
# book_appointment('Alice Smith', 'Dr. John Doe', None)
#
# display_appointments()

# Output displayed after running the above code:
# The program accepted and stored None as the appointment time.

# ----- VERIFYING appointment_time=None FOR THE AI-GENERATED CODE -----:

# appointments = []
#
# # Function to add an appointment
# def book_appointment(patient_name, practitioner_name, appointment_time):
#
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#
#     appointments.append(appointment)
#
# # Add some appointments
# book_appointment("Alice Smith", "Dr Brown", None)
#
# # Display all appointments
# for appointment in appointments:
#     print("Patient:", appointment["patient"])
#     print("Practitioner:", appointment["practitioner"])
#     print("Time:", appointment["time"])
#     print()

# Output displayed after running the above code:
# The program accepted and stored None as the appointment time.


