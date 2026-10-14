employee = {"name":"Dinal" , "age":8 , "salary": 50000}
print(f"His name is {employee["name"]} and his age is {employee["age"]}. He gets {employee["salary"]} salary.")


product = {"name":"laptop", "price":180000, "stock":50}
# stock_status = "In stock" | "low stock" | "out of stock"
if product["stock"]>5:
    product["stock_status"] = "In stock"
elif product["stock"]>0:
    product["stock_status"] = "low stock"
else:
    product["stock_status"] = "out of stock"

print(product)



