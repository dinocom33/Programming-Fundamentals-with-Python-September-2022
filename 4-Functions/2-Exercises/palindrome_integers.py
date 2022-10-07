input_numbers = input().split(", ")

for n in input_numbers:
    if n == n[::-1]:
        print("True")
    else:
        print("False")
