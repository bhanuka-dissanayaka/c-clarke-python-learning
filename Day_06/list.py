book_names = ["Science" , "Maths" , "History" , " Religion"] # Use plural names when naming a list
print([book_names[0]])
book_names[3] = "Geography"
print(book_names[-2])

for book_name in book_names:
    print(f"Book name is{book_name}")

print(len(book_names))

book_names.append("Atomic Habits")
print(book_names[-1])

# Swapping values of two variables. This is a IQ Question in Interviews -------------
a = 8
b = 7
a =  (a+b)
b = a - b
a = a -b
print(f"a: {a} and b: {b}")

a = 8
b = 7
a,b = b,a  # Using Python
#--------------------------------------------------------

# Swapping in a list
print(f"Before Swapping : {book_names}")
book_names[0] , book_names[-1] = book_names[-1] , book_names[0]
print(f"After Swapping : {book_names}")

# Inserting to list
book_names.insert(1,"New Book")
print(f"After Inserting : {book_names}")

# Delete from list using Index
del book_names[0]
print(f"After Deleting : {book_names}")

# Delete from list using Value
book_names.remove("New Book")
print(f"After Removing : {book_names}")

# Check weather an element is inside a list
print("Maths" in book_names)
print("Mat" in book_names)

# --------------------------------------------------------

numbers = []
for i in range(0,11):
    numbers.append(i)
print("list : ",numbers)

total = 0
for number in numbers:
    total += number
print(f"Sum is {total}")

# --------------------------------------------------------
sleep_hours = []
week_days = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
for i in range(0,7):
    time = int(input(f"Enter your sleeping time for Day {week_days[i]} : "))
    sleep_hours.append(time)

avg_hours = sum(sleep_hours)/len(sleep_hours)
print(f"You sleep around {avg_hours:.2f} hours daily")