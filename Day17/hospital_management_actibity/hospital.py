from Day17.hospital_management_actibity.appointment import Appointment
from Day17.hospital_management_actibity.doctor import Doctor
from Day17.hospital_management_actibity.patient import Patient

class Hospital:
    def __init__(self, hospital_name: str):
        self.hospital_name = hospital_name
        self.patients: list[Patient] = []
        self.doctors: list[Doctor] = []
        self.appointments: list[Appointment] = []


    def register_patient(self, patient: Patient):
        self.patients.append(patient)

    def register_doctor(self, doctor: Doctor):
            self.doctors.append(doctor)

    def display_patients(self):
        print(f"Patients registered at {self.hospital_name}:")
        for patient in self.patients:
            print(
                f"Name: {patient.name}, "
                f"Age: {patient.age}"
                f"Gender: {patient.gender}, "
                f"Contact No: {patient.contact_number}"

            )
    def display_doctors(self):
        print(f"Doctors registered at {self.hospital_name}:")
        for doctor in self.doctors:
            print(
                f"Name: {doctor.name}, "
                f"Doc ID: {doctor.doctor_id}"
                f"Specialization: {doctor.specialization}, "
                f"Consultation_fee: {doctor.consultation_fee}"

            )
    def search_patient(self, name: str):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

    def book_appointment(self, new_appointment: Appointment ):
        for appointment in self.appointments:
            if appointment.date == new_appointment.date and appointment.time == new_appointment.time and appointment.doctor == new_appointment.doctor:
                print("This doctor already has an appointment in this time.")
                return

        patient_ids = [patient.patient_id for patient in self.patients]
        for doctor in self.doctors:
            if doctor.doctor_id == new_appointment.doctor.doctor_id and new_appointment.patient.patient_id in patient_ids:
                self.appointments.append(new_appointment)
                print("Appointmetn booked")
                return

        print("Patient or Doctor Not Registered")
        # raise ValueError("Patient or Doctor Not Registered")




doctor1 = Doctor("Kamal Perera", "D001", "Cardiologist", 2500.00)
doctor2 = Doctor("Nimal Silva", "D002", "Cardiologist", 2000.00)

patient1 = Patient("P001","Kalana" , 85 , "male" , "084518745")
patient2 = Patient("P002","Sunimal" , 89 , "male" , "0484855151")
patient3 = Patient("P003","Saduni" , 87 , "female" , "0145152105")
patient4 = Patient("P004","Niluni" , 86 , "female" , "5847/451")
patient5 = Patient("P005","Kalani" , 87 , "female" , "25689412")

hospital = Hospital("ABC Hospitals")
hospital.register_patient(patient1)
hospital.register_patient(patient2)
hospital.register_patient(patient3)
hospital.register_patient(patient4)
hospital.register_patient(patient5)

search = hospital.search_patient("Kalana")
print(search)
search = hospital.search_patient("Kalanasef")
print(search)

print("--------------------------")

hospital.register_doctor(doctor1)
hospital.register_doctor(doctor2)

unregistered_doctor = Doctor("Sunil Fernando", "D003", "Neurologist", 3500.00)
unregistered_patient = Patient("P008","Kalani" , 87 , "female" , "25689412")

appointment1 = Appointment("AP001", patient1, unregistered_doctor, "2025-10-05", "8.30")
appointment2 = Appointment("AP002", unregistered_patient, doctor2, "2025-10-08", "8.30")
appointment3 = Appointment("AP001", patient1, doctor1, "2025-10-05", "8.30")
appointment4 = Appointment("AP002", patient5, doctor2, "2025-10-08", "8.30")
hospital.book_appointment(appointment1)
hospital.book_appointment(appointment2)
hospital.book_appointment(appointment3)
hospital.book_appointment(appointment4)
hospital.book_appointment(appointment3)



