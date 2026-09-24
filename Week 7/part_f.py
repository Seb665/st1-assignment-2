from patient_practitioner import Patient, Practitioner
from ai_on import Appointment # Change ai_on to part_g to verify that the refactored code from part_g still passes the same tests.

# Test 1: Creating the valid objects:

patient1 = Patient("P001", "Sebastian", "01/01/2000", "0400000000")

practitioner1 = Practitioner("PR001", "Dr Smith", "General Practice")

appointment1 = Appointment("A001", "24/09/2026 10:00", patient1, practitioner1, "General consultation")

print("Starting status:", appointment1.status)

# Test 2 - Test invalid input

try:
    bad_appointment = Appointment("", "24/09/2026 11:00", patient1, practitioner1)
except ValueError as error:
    print("Invalid input test:", error)

# Test 3 - Cancel a scheduled appointment

appointment1.cancel()

print("Status after cancellation:", appointment1.status)

# Test 4 - Try to cancel the same appointment again

try:
    appointment1.cancel()
except ValueError as error:
    print("Repeated cancellation test:", error)

