budget = int(input())

command = input()
total_price = 0

while command != "End":
    current_price = int(command)
    total_price += current_price
    if total_price > budget:
        print("You went in overdraft!")
        break
    command = input()

if total_price <= budget:
    print("You bought everything needed.")
