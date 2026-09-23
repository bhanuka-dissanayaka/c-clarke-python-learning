book_names = ["Science" , "Maths" , "History" , " Religion"] # Use plural names when naming a list
print([book_names[0]])
book_names[3] = "Geography"
print(book_names[-2])

for book_name in book_names:
    print(f"Book name is{book_name}")

print(len(book_names))

book_names.append("Atomic Habits")
print(book_names[-1])