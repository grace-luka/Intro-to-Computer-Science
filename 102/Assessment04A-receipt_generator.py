#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 04A
#   References:
#   Time: 25 minutes

company_name = input('Enter company name: ')
city_state = input('Enter company city/state: ')
cashier_name = input('Enter cashier name: ')

item_1_name = input('Purchased item 1 name: ')
item_1_price = float(input('Purchased item 1 price: '))

item_2_name = input('Purchased item 2 name: ')
item_2_price = float(input('Purchased item 2 price: '))

item_3_name = input('Purchased item 3 name: ')
item_3_price = float(input('Purchased item 3 price: '))

ending_message = input('Enter your favorite ending message: ')

tota = (item_1_price + item_2_price + item_3_price)
total = (f'{tota :.2f}')


print(f'         RECEIPT GENERATOR         ')
print(f'------------------------------------')
print(f'    {company_name}    ')
print(f'    {city_state}      ')
print(f'====================================')
print(f'    Your cashier was: {cashier_name} ')
print(f'    Welcome Valued Customer         ')
print(f'====================================')
print(f'    Item Name     Item Price        ')
print(f'    {item_1_name} ${item_1_price}   ')
print(f'    {item_2_name} ${item_2_price}   ')
print(f'    {item_3_name} ${item_3_price}   ')
print(f'====================================')
print(f'    Total Cost of Order: ${total}   ')
print(f'====================================')
print(f'    {ending_message}           ')
print(f'------------------------------------')
