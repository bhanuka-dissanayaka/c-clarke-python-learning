nums = [10,2,3,5]
nums_2 = nums
nums_2.append(200)
print(nums)

nums_3 = nums[:]
del nums_3[0]
print(nums)
print(nums_3)
