temperature_of_week_by_day = [[0.0 for j in range(3)] for i in range(7)]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print("1. Enter the temperature")
print("2. Check temperature of special time")
print("3. Average temp of a day")
print("4. Check the height temperature of a day")
print("5. Average temp of week")
print("0. Exit")

option = int(input("Input a option : "))

while True:
    if option == 0 :
        break
    if option == 1:
        day_option = int(input("1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday 6.Saturday 7.Sunday "))
        time_option = int(input("1.Morning 2.Afternoon 3.Night "))
        time_temp = int(input("Enter the temp : "))
        temperature_of_week_by_day[day_option - 1][time_option - 1] = time_temp
        print(temperature_of_week_by_day)
    if option == 2:
        day_to_check = int(input("Enter a day to check temperature : "))
        time_to_check = int(input("Enter a time to check temperature : "))
        print(f"Temperature is {temperature_of_week_by_day[day_to_check - 1][time_to_check - 1]}")
    if option == 3:
        day_to_check = int(input("Enter a day to check temperature : "))
        sum_of_day = sum(temperature_of_week_by_day[day_to_check - 1])
        print(f"Average Temperature is {sum_of_day}")
    if option == 4:
        day_to_check = int(input("Enter a day to check temperature : "))
        copy = temperature_of_week_by_day[:].sort(reverse=True)
        day_highest_temp = temperature_of_week_by_day[0]
        print(f"Highest Temperature is {day_highest_temp}")
    if option == 5:
        total_temp = 0
        for i in temperature_of_week_by_day:
            total_temp += sum(i)
        print(f"Average Temperature of week : {total_temp / 7}")








