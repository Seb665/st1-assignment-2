class Patient:
    def __init__ (self, patient_information):
        self.patient_information = patient_information

    def search_information(self):
        pass

    def update_information(self):
        pass

class Practitioner:
    def __init__(self, practitioner_information):
        self.practitioner_information = practitioner_information

    def get_information(self):
        pass

class Appointment:
    def __init__(self, appointment_information, status):
        self.appointment_information = appointment_information
        self.status = status

    def update_status(self):
        pass

    def view_history(self):
        pass

    def detect_duplicate(self):
        pass