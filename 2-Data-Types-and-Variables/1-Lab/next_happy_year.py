year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    year_as_set = set()
    for current_digit in range(len(str(year))):
        year_as_set.add(str(year)[current_digit])
        if len(year_as_set) == len(str(year)):
            is_happy_year = True
            break
print(year)
