number = float(input())

if number == 0:
    print("zero")
elif 0 < abs(number) < 1:
    if number < 0:
        print("small negative")
    else:
        print("small positive")
elif abs(number) < 1000000:
    if number < 0:
        print("negative")
    else:
        print("positive")
else:
    if number < 0:
        print("large negative")
    else:
        print("large positive")
