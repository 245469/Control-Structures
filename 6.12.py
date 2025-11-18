number_of_products = int(input('How many products do you want to buy? '))
product_price = 40
if number_of_products > 2:
    total_price = product_price * 2 + (number_of_products - 2) * (product_price * 0.75)
    print(f'Amount to pay: {total_price}')
else:
    total_price = product_price * number_of_products
    print(f'Amount to pay: {total_price}')