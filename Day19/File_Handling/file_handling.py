file = open("text.txt", "r")

# print(f"First Line : {file.readline()}")
#
# content = file.read()
# print(content)

for line in file:
    print(line)
#
# for line in file:
#     print(line.strip())

file.close()

file2 = open("student_info.txt", 'w')
file2.write("amila , 19 , 02315454\n\n")
file2.write("nisal , 19 , 02315454")
file2.close()


file3 = open("phone_no.txt", "w+")
file3.write("07112885656\n")
file3.write("07874151215\n")
file3.write("08784651423\n")
file3.seek(0)
print(file3.read())

with open("text.txt") as f:
    for line in f:
        print(line)

