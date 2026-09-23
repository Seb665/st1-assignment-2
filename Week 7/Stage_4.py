class Patient:
    def __init__(self, patient_id: str, name: str, date_of_birth: str, contact_details: str):

        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")

        if not name.strip():
            raise ValueError("Invalid patient name")

        if not date_of_birth.strip():
            raise ValueError("Invalid date of birth")

        if not contact_details.strip():
            raise ValueError("Invalid contact details")

        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_details = contact_details

