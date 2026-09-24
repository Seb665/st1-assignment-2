from enum import Enum
from patient_practitioner import Patient, Practitioner # this single linewas manually added so Appointment
# can use the Patient and Practitioner classes stored in the separate patient_practitioner.py file.
# It also makes part_f file much easier to test.


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        date_time: str,
        patient: Patient,
        practitioner: Practitioner,
        notes: str = ""
    ):
        if not appointment_id.strip():
            raise ValueError("Appointment ID cannot be empty")

        if not date_time.strip():
            raise ValueError("Appointment date and time cannot be empty")

        self.appointment_id = appointment_id
        self.date_time = date_time
        self.patient = patient
        self.practitioner = practitioner
        self.notes = notes
        self.status = AppointmentStatus.SCHEDULED

    def cancel(self):
        if self.status != AppointmentStatus.SCHEDULED:
            raise ValueError("Only scheduled appointments can be cancelled")

        self.status = AppointmentStatus.CANCELLED