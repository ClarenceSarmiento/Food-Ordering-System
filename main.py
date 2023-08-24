"""
Food Ordering System

Show Menu
Add Order
Change Order Quantity or Size
Remove Order
Show Orders

"""

from tabulate import tabulate
import pandas as pd
import sys


class FoodOrderSystem:
    def __init__(self, menu_file):
        self.menu = pd.read_csv(menu_file, index_col='CODE')
        self.orders = []

    def show_menu(self):
        print(tabulate(self.menu, headers='keys', tablefmt='pretty'))

    def add_order(self, code: str, size: str, quantity: int):
        try:
            if code in self.menu.index:
                price = self.menu.at[code, size]
                flavor = self.menu.at[code, "FLAVOR"]
                order = {
                    'CODE': code,
                    'SIZE': size,
                    'FLAVOR': flavor,
                    'QUANTITY': quantity,
                    'PRICE': price,
                    'TOTAL PRICE': price * quantity
                }
                for existing_order in self.orders:
                    if existing_order['CODE'] == code and existing_order['SIZE'] == size:
                        existing_order['QUANTITY'] += quantity
                        existing_order['TOTAL PRICE'] += order['TOTAL PRICE']
                        break
                else:
                    self.orders.append(order)
                print('Order added successfully.')
            else:
                raise KeyError
        except KeyError:
            print('Code/Size not found. Order not added.')

    def change_order(self):
        ...

    ...

    def remove_order(self):
        ...

    ...

    def show_orders(self):
        if len(self.orders) != 0:
            print(tabulate(self.orders, headers='keys', tablefmt='pretty'))
        else:
            print('No order added yet.')


def main():
    menu = 'menu.csv'
    food_ordering_system = FoodOrderSystem(menu)
    functions = [
        [1, 'Show Menu'],
        [2, 'Add Order'],
        [3, 'Change Order'],
        [4, 'Remove Order'],
        [5, 'Show Order'],
        [6, 'Exit']
    ]
    print(tabulate(functions, headers=['CODE', 'FUNCTION'], tablefmt='pretty'))
    while True:
        try:
            code = int(input("Enter Code: "))
            if code == functions[0][0]:
                food_ordering_system.show_menu()
            elif code == functions[1][0]:
                while True:
                    try:
                        code, size, quantity = input('Enter Order (CODE | SIZE | QUANTITY): ').upper().split(" ")
                        food_ordering_system.add_order(code, size, int(quantity))
                    except EOFError:
                        break
            elif code == functions[2][0]:
                ...
            elif code == functions[3][0]:
                ...
            elif code == functions[4][0]:
                food_ordering_system.show_orders()
            elif code == functions[5][0]:
                sys.exit('Thank you for Ordering!')
            else:
                print('Code not found.')
        except ValueError:
            sys.exit('Code is not a number.')


if __name__ == "__main__":
    main()
