# Using For Loop
# arr = [0,985,65,65,65,6,65,8,8,6,8]
# # limit=len(arr)-1
# limit2 = len(arr) - 1
#
# for x in range(0, limit2):
#     print("List 1 Iterate")
#     for i in range(0, limit2):
#         print("List 2 Iterate")
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     limit2 -= 1
# print(arr)



# Using While Loop
arr = [0,985,65,65,65,6,65,8,8,71,100,8]
limit2 = len(arr) - 1
x = 0
while x < len(arr):
    print("List 1 Iterate")
    i = 0
    while i < limit2:
        print("List 2 Iterate")
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = i+1
    x += 1
    limit2 -= 1
print(arr)


