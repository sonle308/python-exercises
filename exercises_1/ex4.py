# Grocery App
# Write a programme that
# (1) Allows warehouse employees to enter a list of goods (including names only - using
# a string separated by commas) that are available in his/her shop
# (2) Allows customers to check whether an item is in stock or not by inputting a name:
# just show “Available” or “Out of stock!” on screen

print('Enter a list of goods:')
goods = list(map(lambda str: str.strip(), input().split(',')))

while(True):
    print('Enter name of product:')
    product_name = input()
    if product_name in goods:
        print('Available')
    else:
        print('Out of stock!')
