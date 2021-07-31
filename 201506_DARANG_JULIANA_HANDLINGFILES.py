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

            menu.append(product_code + "," + get_product(product_code)["name"] + "," + quantity_code + "," + str(get_property(product_code, "price") * int(quantity_code)))
            subtotal.append(get_property(product_code, "price") * int(quantity_code))

            total = sum(subtotal)
            continue

    final = []
    for i in menu:
        final.append(i.split(","))
        final.sort()

    with open("receipt.txt", "w") as receipt:
        receipt.write('==\nCODE\t\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL')

        for j in range(len(final)):
            code = final[j][0]
            name = final[j][1]
            quantity = final[j][2]
            subtotal = final[j][3]

            receipt.write(f'\n{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}')

        receipt.write(f'\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t{total}\n== ')

main()
