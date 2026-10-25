from shop import product

while True:
    choice = input(
        "Press 1 to view products :  \n Press 2 to add products : ")
    if choice == "1":
        product.show_products()