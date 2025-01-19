import csv
import csvdb
import datetime

db = csvdb.CSVDBObject("inventory_management", "tables")

inventory_table = db.create_table("inventory", {
    "item_id": (int, True, True),
    "item_name": (str, True, False),
    "item_price": (float, True, False)
})

sales_table = db.create_table("sales", {
    "sale_id": (int, True, True),
    "item_id": (int, True, False),
    "customer_id": (int, True, False),
    "employee_id": (int, True, False),
    "sale_date": (str, True, False),
    "quantity": (int, True, False),
    "total_price": (float, False, False)
})

customer_table = csvdb.CSVTable(db, "customer", {
    "customer_id": (int, True, True),
    "customer_name": (str, True, False),
    "date_joined": (datetime.date, False, False)
})


def inventory_management():
    print("Inventory Management")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_id = int(input("Enter item ID: "))
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
    if choice == 2:
        item_id = int(input("Enter item ID: "))
    if choice == 3:
        pass
    if choice == 4:
        exit()

def sales_management():
    print("Sales Management")
    print("1. Add Sale")
    print("2. View Sales")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        sale_id = int(input("Enter sale ID: "))
        item_id = int(input("Enter item ID: "))
        sale_date = input("Enter sale date: ")
        quantity = int(input("Enter quantity: "))
        total_price = float(input("Enter total price: "))
    if choice == 2:
        pass


def customer_management():
    pass


def employee_management():
    pass


def main():
    # Business Management Program using CSV
    print("Business Management Program")
    print("1. Inventory Management")
    print("2. Sales Management")
    print("3. Customer Management")
    print("4. Employee Management")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        inventory_management()
    if choice == 2:
        sales_management()
    if choice == 3:
        customer_management()
    if choice == 4:
        employee_management()
    if choice == 5:
        exit()
