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
    order = []
    subtotal = []

    while True:
        product_code = input("What is your order? ")

        if product_code != "/":
            quantity_code = input("Quantity: ")

            order.append(product_code + "," + get_product(product_code)["name"] + "," + quantity_code + "," + str(get_property(product_code, "price") * int(quantity_code)))
            subtotal.append(get_property(product_code, "price") * int(quantity_code))

            total = sum(subtotal)

            continue

        elif product_code == "/":
            break

    final = []
    for i in order:
        final.append(i.split(","))
        final.sort()

    with open("receipt.txt", "w") as receipt:
        receipt.write('==\nCODE\t\t\t\t\t\t\tNAME\t\t\t\t\t\tQUANTITY\t\t\t\t\t\tSUBTOTAL')

        for j in range(len(final)):
            code = final[j][0]
            name = final[j][1]
            quantity = final[j][2]
            subtotal = final[j][3]

            receipt.write(f'\n{code}\t\t\t\t{name}\t\t\t\t\t{quantity}\t\t\t\t\t{subtotal}')

        receipt.write(f'\n\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{total}\n== ')

main()
