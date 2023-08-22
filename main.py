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
    orders = {}
    table = tabulate(get_menu(), headers='keys', tablefmt='pretty')
    while True:
        try:
            code, size, quantity = input("Enter Code, Size, and Quantity: ").upper().split(" ")
            flavor, price = get_order(code, size, int(quantity))
            if flavor not in orders:
                orders[flavor] = price
            else:
                orders[flavor] += price
        except EOFError:
            for order in orders:
                print(order)
            break



def get_menu():
    menu = []
    try:
        with open('menu.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                menu.append(row)
        return menu
    except FileNotFoundError:
        sys.exit('CSV file does not exist.')


def get_order(code: str, size: str, quantity: int):
    sizes = ['SMALL', 'MEDIUM', 'LARGE']
    for item in get_menu():
        if item['CODE'] == code and size in sizes:
            flavor = item['FLAVOR']
            price = int(item[size]) * quantity
            return flavor, price






if __name__ == "__main__":
    main()
