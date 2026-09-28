nums = [10,2,3,5]
nums_2 = nums[:]
nums_3 = nums[0:2]  # [Start:End] list slicing
nums_4 = nums[0:-1]  # [Start:End] list slicing
print(nums_3)
print(nums_4)

letters = ["A","V","C","D","E"]
letters_sliced = letters[1:5:2]   # [start:end:step]
letters_reversed = letters[::-1]  # Reversing an array
print("letters_sliced : ",letters_sliced)
print("letters_reversed : ",letters_reversed)
