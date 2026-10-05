price_list = [100,200,300,400, 500]
price= [(i/100 *110) for i in price_list]
print("price",price)
print("price list",price_list)
price_list = [(price+price*0.1) for price in price_list]
print("price list",price_list)
