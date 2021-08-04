products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products.get(code)

def get_property(code, property):
    return products[code][property]

def main():
    menu = []
    orders = {}
    subtotal = []

    while True:
        order = input("Order, Quantity: ")

        if order == "/":
            break

        elif "," not in order:
            print("Invalid format.")
            continue

        elif order != "/":
            product_code = order.split(",")[0]
            quantity_code = order.split(",")[1]

        if product_code in orders:
            orders[product_code] += int(quantity_code)
        else:
            orders[product_code] = int(quantity_code)

    for i in range(len(orders)):
        total_product = list(orders.keys())[i]
        quantity = list(orders.values())[i]

        menu.append(total_product + "," + get_product(total_product)["name"] + "," + str(quantity) + "," + str(get_property(total_product, "price") * int(quantity)))
        subtotal.append(get_property(total_product, "price") * int(quantity))

        total = sum(subtotal)

    final = []
    for j in menu:
        final.append(j.split(","))
        final.sort()

    with open("receipt.txt", "w") as receipt:
        receipt.write('==\nCODE\t\t\t\tNAME\t\t\tQUANTITY\t\tSUBTOTAL')

        for k in range(len(final)):
            code = final[k][0]
            name = final[k][1]
            quantity = final[k][2]
            subtotal = final[k][3]

            receipt.write(f'\n{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}')

        receipt.write(f'\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t{total}\n== ')

main()
