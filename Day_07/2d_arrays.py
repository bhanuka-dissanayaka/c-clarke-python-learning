two_dim_arr = [['x','x','x','x'],
               ['x','x','x'],
               ['x','x','x']]

print(len(two_dim_arr[0]))
two_dim_arr[0][1] = 'y'
print(two_dim_arr)


for i in two_dim_arr:
    for x in i:
        print(x)