items = input().split("|")
budget = float(input())

ticket_price = 150
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
money_left = budget
total_spend = 0
total_sell = 0
new_prices_lst = []

for item in items:
    current_item = item.split("->")
    if money_left < float(current_item[1]):
        continue
    elif current_item[0] == "Clothes" and float(current_item[1]) <= clothes_max_price:
        total_spend += float(current_item[1])
        money_left -= float(current_item[1])
        total_sell += float(current_item[1]) * 1.4
        new_prices_lst.append("%.2f" % (float(current_item[1]) * 1.4))
    elif current_item[0] == "Shoes" and float(current_item[1]) <= shoes_max_price:
        total_spend += float(current_item[1])
        money_left -= float(current_item[1])
        total_sell += float(current_item[1]) * 1.4
        new_prices_lst.append("%.2f" % (float(current_item[1]) * 1.4))
    elif current_item[0] == "Accessories" and float(current_item[1]) <= accessories_max_price:
        total_spend += float(current_item[1])
        money_left -= float(current_item[1])
        total_sell += float(current_item[1]) * 1.4
        new_prices_lst.append("%.2f" % (float(current_item[1]) * 1.4))

profit = total_sell - total_spend
budget = total_sell + money_left
print(*new_prices_lst, sep=" ")
print(f"Profit: {profit:.2f}")
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
