number = int(input())

for barcodes in range(number):
    current_barcode = input()
    current_string = ""
    product_group = ""
    if current_barcode[0] == "@" and current_barcode[1] == "#":
        for bar in range(len(current_barcode)):
            if current_barcode[bar] != "@" and current_barcode[bar] != "#" and current_barcode[bar] != "":
                current_string += current_barcode[bar]
            if current_barcode[bar].isnumeric():
                product_group += str(current_barcode[bar])
        if product_group == "":
            product_group = "00"
    if current_string.isalnum() and len(current_string) >= 6:
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
