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
        self.total_price = 0

    def show_menu(self):
        print(tabulate(self.menu, headers='keys', tablefmt='pretty'))

    def add_order(self, code: str, size: str, quantity: int):
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
            return
        raise KeyError

    def change_order(self, code, to_change):  # Changes here is needed!!!
        for order in self.orders:
            try:
                if order['CODE'] == code and to_change == 'SIZE':
                    new_size = str(input('New size (REG/MD/LRG): ').upper())
                    new_price = self.menu.at[code, new_size]
                    order['SIZE'] = new_size
                    order['PRICE'] = new_price
                    order['TOTAL PRICE'] = new_price * order['QUANTITY']
                    print('Order Size changed successfully.')
                    return
                elif order['CODE'] == code and to_change == 'QUANTITY':
                    new_quantity = int(input('New Quantity: '))
                    order['QUANTITY'] = new_quantity
                    order["TOTAL PRICE"] = order['PRICE'] * new_quantity
                    print('Order Quantity changed successfully.')
                    return
            except KeyError:
                print('Invalid Size, must be (REG/MD/LRG).')
                return
            except ValueError:
                print('Quantity is not a number.')
                return
        raise ValueError

    def remove_order(self, code, size):
        for order in self.orders:
            if order['CODE'] == code and order['SIZE'] == size:
                self.orders.remove(order)
                self.total_price = 0
                print('Order removed successfully.')
                break
        else:
            print('Order not found.')

    def show_orders(self):
        if len(self.orders) != 0:
            print(tabulate(self.orders, headers='keys', tablefmt='pretty'))
            for order in self.orders:
                self.total_price += order['TOTAL PRICE']
            print(f"Total Price: P{self.total_price:,.2f}")
        else:
            print('No order added yet.')


def main():
    menu = 'menu.csv'
    food_ordering_system = FoodOrderSystem(menu)
    functions = [
        [1, 'Show Menu'],
        [2, 'Add Order'],
        [3, 'Change Order (Size | Quantity)'],
        [4, 'Remove Order'],
        [5, 'Show Order'],
        [6, 'Exit']
    ]
    print(tabulate(functions, headers=['CODE', 'FUNCTION'], tablefmt='pretty'))
    while True:
        try:
            code = int(input("Enter Function Code: "))
            if code == functions[0][0]:
                food_ordering_system.show_menu()
            elif code == functions[1][0]:
                while True:
                    try:
                        code, size, quantity = str(input('Enter Order (CODE | SIZE | QUANTITY): ')).upper().split(" ")
                        food_ordering_system.add_order(code, size, int(quantity))
                    except ValueError:
                        pass
                    except KeyError:
                        print('Order Code/Size not found. Order not added.')
                    except EOFError:
                        break
            elif code == functions[2][0]:
                print(tabulate((['Size'], ['Quantity']), headers=['TO CHANGE'], tablefmt='pretty'))
                while True:
                    try:
                        code, to_change = input('Order Code and what to change (Size | Quantity): ').upper().split(" ")
                        food_ordering_system.change_order(code, to_change)
                    except ValueError:
                        print('Order not found.')
                    except EOFError:
                        break
            elif code == functions[3][0]:
                code, size = input('Order Code and Size to remove: ').upper().split(" ")
                food_ordering_system.remove_order(code, size)
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
