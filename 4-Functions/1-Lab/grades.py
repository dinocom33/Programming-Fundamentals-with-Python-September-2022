def solve(number):
    if number < 3:
        return "Fail"
    elif number < 3.50:
        return "Poor"
    elif number < 4.50:
        return "Good"
    elif number < 5.50:
        return "Very Good"
    elif number < 6:
        return "Excellent"


current_grade = float(input())
print(solve(current_grade))
