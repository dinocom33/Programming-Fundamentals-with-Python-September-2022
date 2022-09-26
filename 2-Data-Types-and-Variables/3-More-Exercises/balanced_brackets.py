number_of_lines = int(input())

brackets_found = []
is_balanced = True

for current_line in range(number_of_lines):
    bracket = input()
    if bracket == "(":
        brackets_found.append(bracket)
    elif bracket == ")":
        brackets_found.append(bracket)
    for i in range(len(brackets_found) - 1):
        if brackets_found[i] == brackets_found[i+1]:
            is_balanced = False
            break
if len(brackets_found) % 2 != 0:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
