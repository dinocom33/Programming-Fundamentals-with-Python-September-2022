import re

number_of_barcodes = int(input())

pattern = r"@[#]{1,}(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]{1,}"

for num_barcode in range(number_of_barcodes):
    current_barcode = input()
    result = re.finditer(pattern, current_barcode)
    product_group = ""
    for bar in result:
        barcode = bar["barcode"]
        for digit in barcode:
            if digit.isdigit():
                product_group += digit
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    if product_group == "":
        print("Invalid barcode")
