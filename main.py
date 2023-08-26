"""
NAME
    Food Ordering System

DESCRIPTION
    This program takes order from the user.

FUNCTIONS
    show_menu()
        Prints the tabulated form of menu.

    add_order(code: str, size: str, quantity: int)
        Append the user's order to list of orders.

    change_order(code: str, to_change: str)
        Changes the user's specified order its size or quantity.

    remove_order(code: str, size: str)
        Removes the user's order based on its order code and size.

    show_orders()
        Prints the tabulated form of list of orders with its overall price.
"""

from tabulate import tabulate
import pandas as pd
import sys


class FoodOrderSystem:
    """
    A class representing a food ordering system.

    Attributes:
        menu (DataFrame): Menu data containing food items and their details.
        orders (list): List of ordered items.
        total_price (float): Total price of all orders combined.
    """
    def __init__(self, menu_file):
        """
        Initialize the FoodOrderSystem with menu data and empty order list.

        Args:
            menu_file (str): Filepath to the CSV menu data.
        """
        self.menu = pd.read_csv(menu_file, index_col='CODE')
        self.orders = []
        self.total_price = 0

    def show_menu(self):
        """
        Shows the tabulated form of menu.
        """
        print(tabulate(self.menu, headers='keys', tablefmt='pretty'))

    def add_order(self, code: str, size: str, quantity: int):
        """
        Add user's order to list of orders.

        Args:
            code (str): the string for order code to be added.
            size (str): the string for order size (REG/MD/LRG).
            quantity (int): the integer for order's quantity.

        Raises:
            KeyError: code or size not found.

        Returns:
            orders (dict): code, size, flavor, quantity, price, total price
        """
        if code in self.menu.index and size in ['REG', 'MD', 'LRG']:
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
        raise ValueError

    def change_order(self, code: str, to_change: str):
        """
        Changes the user's specified order its size or quantity.

        Args:
            code (str): the string for order code to be changed.
            to_change (str): the string for order size or quantity to be changed.

        Raises:
            KeyError: Size must be str, not int. Cannot locate at menu file.
            ValueError: Quantity must be int, not str.
            ValueError: code is not found.

        Returns:
            orders (dict): new size, new price, new quantity
        """
        if self.orders:
            for order in self.orders:
                if order['CODE'] == code:
                    if to_change == 'SIZE':
                        try:
                            new_size = str(input('New size (REG/MD/LRG): ').strip().upper())
                            if new_size in ['REG', 'MD', 'LRG']:
                                new_price = self.menu.at[code, new_size]
                                order['SIZE'] = new_size
                                order['PRICE'] = new_price
                                order['TOTAL PRICE'] = new_price * order['QUANTITY']
                                print('Order Size changed successfully.')
                            else:
                                print('Invalid Size, should be "REG", "MD", "LRG".')
                        except ValueError:
                            print('Invalid Size, must be a string.')
                    elif to_change == 'QUANTITY':
                        try:
                            new_quantity = int(input('New Quantity: '))
                            if new_quantity > 0:
                                order['QUANTITY'] = new_quantity
                                order["TOTAL PRICE"] = order['PRICE'] * new_quantity
                                print('Order Quantity changed successfully.')
                            else:
                                print('Quantity must be a positive number.')
                        except ValueError:
                            print('Invalid Quantity, must be a number.')
                    return
            raise ValueError
        else:
            print('No orders to change yet.')
            return False

    def remove_order(self, code: str, size: str):
        """
        Removes the user's order based on its order code and size.

        Args:
            code (str): the string for order code to be removed.
            size (str): the string for order size to be removed.
        """
        if self.orders:
            for order in self.orders:
                if order['CODE'] == code and order['SIZE'] == size:
                    self.orders.remove(order)
                    print('Order removed successfully.')
                    break
            else:
                print('Order not found.')
        else:
            print('No orders to remove yet.')

    def show_orders(self):
        """
        Prints the tabulated form of list of orders with its overall price.
        """
        if self.orders:
            print(tabulate(self.orders, headers='keys', tablefmt='pretty'))
            self.total_price = sum(order['TOTAL PRICE'] for order in self.orders)
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
            if code == functions[-1][0]:
                sys.exit('Thank you for ordering!')
            elif code in range(1, len(functions)):
                if code == functions[0][0]:
                    food_ordering_system.show_menu()
                elif code == functions[1][0]:
                    while True:
                        try:
                            code, size, quantity = input('Enter Order (CODE | SIZE | QUANTITY): ').split()
                            food_ordering_system.add_order(code.strip().upper(), size.strip().upper(), int(quantity))
                        except ValueError:
                            print('Invalid Input. Order not added.')
                        except EOFError:
                            break
                elif code == functions[2][0]:
                    print(tabulate((['Size'], ['Quantity']), headers=['TO CHANGE'], tablefmt='pretty'))
                    try:
                        code, to_change = input('Order Code and what to change (Size | Quantity): ').split()
                        food_ordering_system.change_order(code.strip().upper(), to_change.strip().upper())
                    except ValueError:
                        print('Order not found.')
                    except EOFError:
                        break
                elif code == functions[3][0]:
                    try:
                        code, size = input('Order Code and Size to remove: ').upper().split(" ")
                        food_ordering_system.remove_order(code, size)
                    except EOFError:
                        break
                elif code == functions[4][0]:
                    food_ordering_system.show_orders()
            else:
                print('Code not found.')
        except ValueError:
            sys.exit('Invalid Input. Please enter a number.')


if __name__ == "__main__":
    main()
