arr = [0,985,65,65,65,6,65,8,8,6,8]
limit=len(arr)-1
print(limit)

for x in range(0, limit):
    print("List 1 Iterate")
    for i in range(0, limit):
        print("List 2 Iterate")
        print(i)
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    i=i+1

print(arr)