class Patient:
    def __init__(self,patient_id:str, name: str, age: int, gender: str, contact_number: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number

    def display_details(self):
        print(f"{self.name:<10}  {self.age:<10}  {self.gender:<10}  {self.contact_number:<10}")

    def update_contact(self, new_contact: str):
        self.contact_number = new_contact


if __name__=="__main__":
    patient1 = Patient("P001","Kalana", 85, "male", "084518745")
    patient2 = Patient("P002","Sunimal", 89, "male", "0484855151")
    patient3 = Patient("P003","Saduni", 87, "female", "0145152105")

    print(f"====Patient Details====")
    print(f"{patient1.name:<10}  {patient1.age:<10}  {patient1.gender:<10}  {patient1.contact_number:<10}")
    print(f"{patient2.name:<10}  {patient2.age:<10}  {patient2.gender:<10}  {patient2.contact_number:<10}")
    print(f"{patient3.name:<10}  {patient3.age:<10}  {patient3.gender:<10}  {patient3.contact_number:<10}")

    patient1.update_contact("2154148125")
    patient2.update_contact("854128712")
    patient3.update_contact("56230541215")

    print("---Updated Details---")
    patient1.display_details()
    patient2.display_details()
    patient3.display_details()

