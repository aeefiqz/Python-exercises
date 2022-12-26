#Solve computational problems using structured programming. Do NOT use global variables
import random
def read_file(filename):
    sales = {}  # create an empty dictionary
    with open(filename, 'r') as f:  # open the file in read mode
        for line in f:  # iterate over the lines in the file
            key, value = line.strip().split()  # split the line into a key and a value
            if key in sales:  # check if the key already exists in the dictionary
                sales[key] += int(value)  # add the new value to the existing value for the key
            else:
                sales[key] = int(value)  # add the key-value pair to the dictionary
    return sales

def update_file(filename,sales):
    salesDict = {}
    with open(filename, 'r') as f:
        for eachline in f:
            eachline = eachline.strip().split()
            if eachline:
                key,value = eachline
                salesDict[key] = int(value)

    with open(filename, 'w') as f:
        for k,v in sales.items():
        # if k in salesDict.keys():
            if k in salesDict:
                salesDict[k] += int(v)
            else:
                salesDict[k] = int(v)

        for k,v in salesDict.items():
            f.write(f"{k} {v}\n")

def getOneSale(item_prices):
    sale = {}
    for key, _ in item_prices.items():
        quantity = int(input(f"Enter the quantity sold for {key}: "))
        sale[key] = quantity
    return sale

def getRandomSale(item_prices):
    sale = {}
    for k,v in prices.items():
        if random.choice([True,False]):
            qty = random.randint(1,15)
            
            sale[k] = qty
    return sale

def totalSales(sale,prices):
    total_sale = 0
    for k,v in prices.items():
        if k in sale:
            qty = sale.get(k)
            total_price = int(v) * qty
            total_sale += total_price
            print(f"{qty} X {k}\t = ${total_price:.2f}")
    print(f"Total\t\t = ${total_sale:.2f}")
                       


# file = 'sales.txt'
# file2 = 'salesToDate.txt'
# sales = read_file('sales.txt')
# print(sales)
# updated_sales = update_file('salesToDate.txt',sales)

prices = {'pencil': 1.85, 'pen': 1.90, 'notebook': 0.90, 'lead': 2.50}

#item_sale = getOneSale(prices)

item_sale2 = getRandomSale(prices)
print(item_sale2)
total_sales = totalSales(item_sale2,prices)