# word = input("Enter a word : ")
# word_reversed = word[::-1]
#
# if word ==word_reversed:
#     print("It is a palindrome word")
# else:
#     print("It is not a palindrome word")
#


word = input("Enter a word : ")
i=0
while i < len(word)/2:
    if word[i] !=word[-(i+1)]:
        print("It is not a palindrome word")
        break
    i+=1
print("It is not a palindrome word")
