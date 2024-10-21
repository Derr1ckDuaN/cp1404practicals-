total_price = 0
number_product = int(input("Enter the number of products:"))

for i in range(number_product):
    price = float(input("Enter the price of product"))
    total_price += price
print("Total price is:$",total_price)

if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount
    print("discount number is:$",discount)
    
print("Final total price after discount is:$",total_price)
