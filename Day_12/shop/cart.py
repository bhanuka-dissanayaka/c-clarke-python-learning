cart_items = []

def add_to_cart(product , quantity):
    cart_items.append({"product" : product , "quantity":quantity})
    print(f"{product["name"]} * {quantity} added to cart successfully")

def view_cart():
    for cart_item in cart_items:
        print(f"{cart_item["product"]["name"]} - {cart_item["quantity"]}")
        print(f"price = {cart_item["product"]["price"]*cart_item["quantity"]}")

if __name__=="__main__":
    add_to_cart({"id":1,"name":"Rice" , "price":200}, 2)
    add_to_cart({"id":2,"name":"Biscuit", "price":140}, 2)
    view_cart()