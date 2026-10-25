
x = "1234435x"

print(x.isdigit())
print(x.count("3"))
print(x.replace("3", "Hello"))
print(x.isalpha())
print(x.isalnum())
print("===========================")

mail = "test@gmail.com"

if "@" in mail:
    print("yes")

print(mail.startswith("t"))
print(mail.endswith(".com"))