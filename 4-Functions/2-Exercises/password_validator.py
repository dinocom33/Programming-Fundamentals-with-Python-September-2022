def password_validator(password):
    digit_counter = 0
    is_password_length = False
    is_password_consist = False
    is_password_two_digits = False
    if 6 <= len(password) < 11:
        is_password_length = True
    for element in password:
        if 48 <= ord(element) <= 57 or 64 <= ord(element) <= 90 or 97 <= ord(element) <= 122:
            is_password_consist = True
        else:
            is_password_consist = False
            break
    for digit in password:
        if digit.isnumeric():
            digit_counter += 1
            if digit_counter >= 2:
                is_password_two_digits = True
    return is_password_length, is_password_consist, is_password_two_digits


input_password = input()
result = password_validator(input_password)

if not result[0]:
    print("Password must be between 6 and 10 characters")
if not result[1]:
    print("Password must consist only of letters and digits")
if not result[2]:
    print("Password must have at least 2 digits")

if result[0] and result[1] and result[2]:
    print("Password is valid")
