# Bookshop App
# (1) Allows clerks to enter a list of books (including titles and quantities – using a
# dictionary) that are available in his/her shop
# (2) Allows customers to check whether an item is in stock or not by inputting a title:
# just show “N items available” or “Out of stock!” on screen

books = {}
def input_book_quantity():
    try:
        print('Enter quantity:')
        return float(input())
    except:
        print('Quantity must be number')
        input_book_quantity()

def input_next_command():
    try:
        print('Enter 1 to continue or 2 to exit!')
        command = float(input())
        if (command == 1):
            input_book_data()
        else:
            check_book()
    except:
        print('Just enter 1 or 2')
        input_next_command()

def input_book_data():
    print('Enter name of book:')
    name = input()
    quantity = input_book_quantity()
    books[name] = quantity
    input_next_command()
    
def check_book():
    while(True):
        print('Enter name of book to check:')
        name = input()
        if name in books:
            print('%d items available' % books[name])
        else:
            print('Out of stock!')

input_book_data()
