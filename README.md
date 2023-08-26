# Food Ordering System
### Description:
A food ordering system that has the following functions:
- Show Menu
- Add Order
- Change Order (Size or Quantity)
- Remove Order
- Show Orders
#### How the Program Works?
The Program utilizes a python library called `pandas`[^1]. This library is used to read the csv file 
`menu.csv` that contains the menu data. 

The Program also utilizes a python library called `tabulate`[^2]. This library is used to display the
menu and the ordered data in a table.

Show Menu
- This function shows the menu currently in the `menu.csv` to the user.

Add Order
- This function adds the user's order to the orders list.

Change Order
- This function lets the user's change their specified order its size or quantity.

Remove Order
- This function removes user's specified order to remove.

Show Orders
- This function shows all the user's orders with its Overall Price.

### TODO:
#### Download
Download the Repository through Clone Repository or Download Zip
```
git clone https://github.com/clarencesarmiento/Food-Ordering-System.git
```
After download, go to `cmd` and navigate to the folder directory.
```
cd Food-Ordering-System
```
#### Installation
Use [pip](https://pip.pypa.io/en/stable/) to install needed libraries inside
the `requirements.txt`.
```
pip install -r requirements.txt
```
#### Usage
Run the `main.py` using [python](https://www.python.org/).
```
python main.py
```
>[!NOTE]
> The program is case-insensitive.
### References
[^1]: [Pandas](https://pandas.pydata.org/docs/index.html)
[^2]: [Tabulate](https://pypi.org/project/tabulate/)
