food_names = ["Pizza", "Burger" , "Rice" , "Cofee"]
food_prices = [1000,5000,1000,250]

i=0
number = len(food_names)
print("==Food Menu==")
while i < number:
    print(f"{i+1}. {food_names[i]:<10} Rs.{food_prices[i]}")
    i += 1

print("")

orders = []
while True:
    user_choice = int(input("Enter a Food Number : "))
    if user_choice == 0:
        break
    orders.append(user_choice)

total_bill = 0
for i in orders:
    total_bill += food_prices[i-1]

print(f"Total Bill is {total_bill}")