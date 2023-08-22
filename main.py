"""
Food Ordering System

Menu
Order
Checkout
"""

from tabulate import tabulate
import csv
import sys


def main():
    global ordered
    options = [['SHOW', 'menu | order'], ['ORDERS', 'add | change | remove']]
    print(tabulate(options, headers=['FUNCTIONS', 'OPTIONS'], tablefmt='pretty'))
    while True:
        try:
            function, option = input('Command: ').split(' ')
            function = function.upper()
            option = option.lower()
            if function == 'SHOW':
                if option == 'menu':
                    show_menu()
                elif option == 'order':
                    show_order()
                else:
                    raise ValueError
            elif function == 'ORDERS':
                orders = []
                if option == 'add':
                    while True:
                        try:
                            code, size, quantity = input("Enter Code, Size, and Quantity: ").upper().split(" ")
                            orders.append(get_order(code, size, int(quantity)))
                        except EOFError:
                            add_order(orders)
                            break
                elif option == 'change':
                    ...
                elif option == 'remove':
                    ...
                else:
                    raise ValueError
        except ValueError:
            print('Wrong Commands, check your functions or options.')
        except EOFError:
            sys.exit()


def get_menu():
    menu = []
    try:
        with open('menu.csv') as menufile:
            reader = csv.DictReader(menufile)
            for row in reader:
                menu.append(row)
        return menu
    except FileNotFoundError:
        sys.exit('CSV file does not exist.')


def show_menu():
    print(tabulate(get_menu(), headers='keys', tablefmt='pretty'))


def show_order():
    ...
...


def add_order(order_list):
    with open('order.csv', 'w', newline='') as orderfile:
        fieldnames = ['QUANTITY', 'SIZE', 'FLAVOR', 'CODE', 'PRICE', 'TOTAL PRICE']
        writer = csv.DictWriter(orderfile, fieldnames)
        writer.writeheader()
        for order in order_list:
            writer.writerow(order)


#
def get_order(code: str, size: str, quantity: int):
    sizes = ['REG', 'MD', 'LRG']
    for item in get_menu():
        if item['CODE'] == code and size in sizes:
            flavor = item['FLAVOR']
            price = float(item[size]) * int(quantity)
            return {'QUANTITY': quantity, 'SIZE': size, 'FLAVOR': flavor, 'CODE': code, 'PRICE': item[size],
                 'TOTAL PRICE': price}


if __name__ == "__main__":
    main()
