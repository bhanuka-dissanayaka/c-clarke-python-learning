numbers = [1,4,54000,-2,56000007,9999]

def highest_num(index,max_num):
    if numbers[index] > max_num:
        max_num = numbers[index]
    if index == len(numbers)-1:
        return max_num
    return highest_num(index+1,max_num)
print(highest_num(0,numbers[0]))



def reverse_number(number, rev_num):
    if number == 0:
        return rev_num
    digit = number % 10
    rev_num = rev_num*10 + digit
    return reverse_number(number//10,rev_num)

print(reverse_number(100,0))




















