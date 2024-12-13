print('Welcome to supermarket billing simulator')
cart={}
add_items=True

while add_items:
    item_name = input('Enter a product to be added into the cart (enter "Done" to exit):')
    item_name = item_name.upper()  
    if item_name == 'DONE':  
        add_items = False
        break  

    if item_name in cart:
        user_response = input('Item already in cart. Do you want to update cart details? (yes/no): ').lower()
        if user_response == 'yes':
            new_price = float(input('Enter new price of item: '))
            new_quantity = int(input('Enter new quantity of item: '))
            cart[item_name] = {'Price ': new_price, 'Quantity': new_quantity}
        else:
            continue
    else:
        price_of_item = float(input('Enter the item price: '))
        quantity_of_item = int(input('Enter quantity of item: '))
        cart[item_name] = {'Price ': price_of_item, 'Quantity ': quantity_of_item}

print('Here is a summary of your cart:',cart)

total_cost=0

for item in cart:
    price=cart[item]['Price ']
    quantity=cart[item]['Quantity ']
    total_cost+=price*quantity

discounts={
    'SAVE10':{'type':'percentage','amount':10},
    'FIVEOFF':{'type':'fixed','amount':5}
}
discount_code=input('Enter discount code')#discounts[code]

if discount_code in discounts:
    discount_details=discounts[discount_code]
    if discount_details['type']=='percentage':
        discount_calc=total_cost*(discount_details['amount']/100)
    elif discount_details['type']=='fixed':
        total_cost-=discount_details['amount']
    print('Discount Applied!, total cost is =',round(total_cost) )
else:
    print('Invalid Code!')

print('Final Bill Summary:')
for item in cart:
    price=cart[item]['Price ']
    quantity=cart[item]['Quantity ']
    item_total_cost=price*quantity
    print(f"Item name:{item}, Price:{price}, Quantity:{quantity}, Total Cost:{item_total_cost}")
print(f"Grand Total Cost:{round(total_cost)}")