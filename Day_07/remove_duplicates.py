nums = [1,4,5,6,4,4,3,2]
unique_nums = []

for i in nums:
    if i not in unique_nums:
        unique_nums.append(i)

print(unique_nums)