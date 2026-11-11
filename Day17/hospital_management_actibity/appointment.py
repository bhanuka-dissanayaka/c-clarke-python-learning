from Day17.hospital_management_actibity.doctor import Doctor
from Day17.hospital_management_actibity.patient import Patient


class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, doctor: Doctor, date: str, time: str):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
    def display_details(self):
        print(f"{self.patient.name:<15} {self.doctor.name:<15} {self.doctor.specialization:<15} {self.date:<15} {self.time:<15}")

doctor1 = Doctor("Kamal Perera", "D001", "Cardiologist", 2500.00)
doctor2 = Doctor("Nimal Silva", "D002", "Cardiologist", 2000.00)
doctor3 = Doctor("Sunil Fernando", "D003", "Neurologist", 3500.00)

patient1 = Patient("P001","Kalana" , 85 , "male" , "084518745")
patient2 = Patient("P002","Sunimal" , 89 , "male" , "0484855151")
patient3 = Patient("P003","Saduni" , 87 , "female" , "0145152105")

appointment1 = Appointment("AP001", patient1, doctor1, "2025-10-05", "8.30")
appointment2 = Appointment("AP002", patient2, doctor2, "2025-10-08", "8.30")
appointment1.display_details()
appointment2.display_details()
