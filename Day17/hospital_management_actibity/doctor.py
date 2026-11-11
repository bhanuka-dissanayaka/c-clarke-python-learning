class Doctor:
    def __init__(self, name: str, doctor_id: str, specialization: str, consultation_fee: float):
        self.name = name
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def display_details(self):
        print(f"{self.name:<15}  {self.doctor_id:<10}  {self.specialization:<15}  {self.consultation_fee:<10}")

    def update_specialization(self, new_specialization: str):
        self.specialization = new_specialization

if __name__=="__main__":
    doctor1 = Doctor("Kamal Perera", "D001", "Cardiologist", 2500.00)
    doctor2 = Doctor("Nimal Silva", "D002", "Cardiologist", 2000.00)
    doctor3 = Doctor("Sunil Fernando", "D003", "Neurologist", 3500.00)

    print(f"====Doctor Details====")
    print(f"{doctor1.name:<15}  {doctor1.doctor_id:<10}  {doctor1.specialization:<15}  {doctor1.consultation_fee:<10}")
    print(f"{doctor2.name:<15}  {doctor2.doctor_id:<10}  {doctor2.specialization:<15}  {doctor2.consultation_fee:<10}")
    print(f"{doctor3.name:<15}  {doctor3.doctor_id:<10}  {doctor3.specialization:<15}  {doctor3.consultation_fee:<10}")

    doctor1.update_specialization("Neurologist")
    doctor2.update_specialization("Neurologist")
    doctor3.update_specialization("Neurologist")

    print("---Updated Details---")
    doctor1.display_details()
    doctor2.display_details()
    doctor3.display_details()



