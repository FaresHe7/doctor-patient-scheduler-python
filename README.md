# Doctor Patient Booking System

A simple Python OOP project that simulates a clinic booking system where patients can book appointments with a doctor.

## How it works
- Each patient has: name, age, health condition, and preferred booking time.
- The doctor has a list of available working hours.
- Patients can book an appointment if the time is available.
- The system prevents:
  - Booking outside working hours
  - Double booking the same time slot
  - Exceeding the maximum number of patients per day

## Example
```python
clinic = Doctor("clinic Health")

patient_1 = Patient("ahmed", "stomach ache", 20, 9.5)

print(clinic.book(patient_1))
