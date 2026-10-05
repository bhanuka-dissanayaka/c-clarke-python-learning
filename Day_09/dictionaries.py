student = {
    "name" : "supun",
    "age" : 20 ,
    "married" : True ,
    "address" : "kurunegala",
    "contacts" : ["07545421121" , "071545454545"]
}
print(student["name"])
print(student["contacts"][0])

student["contacts"].append("07874545454")

for i in student:
    print(student[i])

for key in student.keys():     # Iterating over the keys
    print(f"key- {key} and value- {student[key]}")

for val in student.values():   # Iterating over the values
    print(f"value- {val}")

for contact in student["contacts"]:
    print(f"contact : {contact}")

for key,val in student.items():  # Iterating using both key and value
    print(f"key - {key} and value - {val}")

student["name"] = "Amal"
print(student["name"])


order = {
    1.5 : "name",
    (1,2,3,4) : "Tuple"
}
# For a key , we can use any immutable data type. even tuples can be used because they are immutable

del student["age"]  # Deleting a value
# student["grades"] we can not do this because there is no key called grade
student["grades"] = ['A','B','A']    # Inserting new key and value