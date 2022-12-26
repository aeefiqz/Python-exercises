# Define a dictionary of menu items with their prices
menu = {
    "B1": {"name": "Chicken briyani", "price": 5.00},
    "B2": {"name": "Mutton briyani", "price": 5.50},
    "B3": {"name": "Fish briyani", "price": 6.00}
}

# Initialize the order number and orders dictionary
order_number = 1
orders = {}

# Run the main menu in a loop
while True:
    # Print the main menu and get the user's choice
    print("ABC Briyani")
    print("1. Place order")
    print("2. Update order")
    print("3. Serve order")
    print("0. Exit")
    print("Enter option: ", end="")
    choice = input()
    print(orders)
    # If the user chose to place an order
    if choice == "1":
        # Initialize the total price
        total_price = 0

        # Print the menu
        print("Menu")
        for item_code, item in menu.items():
            print(f"{item_code} - {item['name']} ${item['price']}")

        # Initialize the order list
        order = []

        # Get the user's order
        while True:
            print("Enter item code and quantity (Press <Enter> key to end): ", end="")
            line = input()

            # If the user presses Enter, break out of the loop
            if line == "":
                break

            # Split the line into item code and quantity
            item_code, quantity = line.split()

            # If the item code is not in the menu, print an error message
            if item_code not in menu:
                print("Invalid item code! Try again.")
                continue

            # Otherwise, add the item to the order list
            order.append([item_code, int(quantity)])

        # Add the order to the orders dictionary
        orders[order_number] = order

        # Print the order
        print(f"\nOrder number {order_number}")
        for item in order:
            item_code, quantity = item
            item = menu[item_code]
            price = item["price"] * quantity
            total_price += price
            print(f"{item_code} {item['name']} X {quantity} = ${price:.2f}")
        print(f"Total price ${total_price:.2f}")

        # Increment the order number
        order_number += 1

    # If the user chose to exit
    elif choice == "0":
        # Break out of the main menu loop
        break