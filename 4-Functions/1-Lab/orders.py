def orders(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2


current_product = input()
current_quantity = int(input())

final_sum = orders(current_product, current_quantity)

print(f"{final_sum:.2f}")
