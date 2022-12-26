def read_file(filename):
    menu_dict = {}
    with open(filename, 'r') as f:
        eachline = f.readlines()
    for line in eachline:
        tokens = line.strip().split(',')
        menu_dict[tokens[0]] = [tokens[1], tokens[2]]
    return menu_dict

def place_order(menu,orders):
    order_number = 1
    print('menu')
    for k,v in menu.items():
        print(f"{k} - {v[0]} {v[1]}")

    while True:
        order = input("Enter item code and quantity (Press <Enter> key to end): ").upper()
        if order == "":
            if order_number in orders.keys():  # check if the current order has any items
                order_number += 1  # increment the order number if there are items in the current order
            else:
                break  # exit the loop if there are no items in the current 
        
        else:
            item_code, qty = order.split(' ')
            if item_code not in menu.keys():
                print("Invalid item code! Try again")
            else:
                if order_number in orders.keys():
                    orders[order_number].append([item_code, int(qty)])
                else:
                    orders[order_number] = [[item_code, int(qty)]]
            order_number += 1
                                 
    return orders

def menu():
    print("ABC Briyani")
    print("1. Place order")
    print("2. Update order")
    print("3. Serve order")
    print("0. Exit.")
    choice = int(input("Enter option: "))
    return choice

def main():
    food_menu = read_file('exercise-5/menu.txt')
    orders = {}  
    while True:
        choice = menu()
        if choice == 0:
            break
        elif choice == 1:
            orders = place_order(food_menu,orders)
            print(orders)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            print("Invalid choice")

main()
