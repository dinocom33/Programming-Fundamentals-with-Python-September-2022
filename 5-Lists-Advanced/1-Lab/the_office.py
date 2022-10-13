happiness = list(map(int, input().split()))
happiness_factor = int(input())

current_happiness = list(map(lambda x: x * happiness_factor, happiness))
happy_employees = list(filter(lambda x: x >= (sum(current_happiness) / len(current_happiness)), current_happiness))

if len(happy_employees) >= len(current_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(current_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(current_happiness)}. Employees are not happy!")
