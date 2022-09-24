year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    year_as_string = str(year)
    if year_as_string[0] != year_as_string[1] and year_as_string[0] != year_as_string[2] and \
            year_as_string[0] != year_as_string[3] and year_as_string[1] != year_as_string[2] and \
            year_as_string[1] != year_as_string[3] and year_as_string[2] != year_as_string[3]:
        is_happy_year = True
print(year)
