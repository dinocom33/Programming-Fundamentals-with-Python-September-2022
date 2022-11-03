products = input().split()
searched_product = input().split()

bakery = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    bakery[key] = int(value)

for product in searched_product:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
