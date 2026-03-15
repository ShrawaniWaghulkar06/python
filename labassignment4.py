# Inventory Stock Analysis System
inventory = []
# Function to add new item
def add_item():
    item = {
        "id": input("Enter Item ID: "),
        "name": input("Enter Item Name: "),
        "stock": int(input("Enter Initial Stock Quantity: ")),
        "price": float(input("Enter Price per Item: ")),
        "sales": 0
    }
    inventory.append(item)
    print("Item added successfully!\n")
# Function to display inventory
def display_inventory():
    print("\n------ Current Inventory ------")
    print("ID\tName\tStock\tPrice")
    for item in inventory:
        print(f"{item['id']}\t{item['name']}\t{item['stock']}\t₹{item['price']}")
    print()
# Function to record sales
def record_sale():
    item_id = input("Enter Item ID to sell: ")
    for item in inventory:
        if item["id"] == item_id:
            quantity = int(input("Enter quantity sold: "))
            if quantity <= item["stock"]:
                item["stock"] -= quantity
                item["sales"] += quantity
                print("Sale recorded successfully!\n")
            else:
                print("Not enough stock available!\n")
            return
    print("Item not found!\n")
# Function to restock item
def restock_item():
    item_id = input("Enter Item ID to restock: ")
    for item in inventory:
        if item["id"] == item_id:
            quantity = int(input("Enter quantity to add: "))
            item["stock"] += quantity
            print("Item restocked successfully!\n")
            return
    print("Item not found!\n")
# Function to show low stock alerts
def low_stock_alert():
    print("\n------ Low Stock Alert (Below 5) ------")
    for item in inventory:
        if item["stock"] < 5:
            print(f"{item['name']} (ID: {item['id']}) is low on stock!")
    print()
# Function to show sales summary
def sales_summary():
    print("\n------ Sales Summary ------")
    total_revenue = 0
    for item in inventory:
        revenue = item["sales"] * item["price"]
        total_revenue += revenue
        print(f"{item['name']} - Sold: {item['sales']}, Revenue: ₹{revenue}")
    print(f"\nTotal Revenue Generated: ₹{total_revenue}\n")
# Main Menu
while True:
    print("========== Inventory Stock Analysis System ==========")
    print("1. Add New Item")
    print("2. View Inventory")
    print("3. Record Sale")
    print("4. Restock Item")
    print("5. Low Stock Alert")
    print("6. Sales Summary")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        display_inventory()
    elif choice == '3':
        record_sale()
    elif choice == '4':
        restock_item()
    elif choice == '5':
        low_stock_alert()
    elif choice == '6':
        sales_summary()
    elif choice == '7':
        print("Exiting system... Thank you!")
        break
    else:
        print("Invalid choice! Try again.\n")