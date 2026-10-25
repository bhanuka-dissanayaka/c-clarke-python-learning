products = [
    {"id":1 , "name":"rice" , "price":200.00},
    {"id": 2, "name": "Dhal", "price": 250.00},
    {"id": 3, "name": "Biscuit", "price": 140.00}

]

def show_products():
    print("Available Products")
    for product in products:
        print(f"{product["id"]} | {product["name"]} | {product["price"]}")

def find_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return product
    return "Product Not Found"

if __name__=="__main__":
    print("Testing")
    show_products()
    print(find_product_by_id(2))