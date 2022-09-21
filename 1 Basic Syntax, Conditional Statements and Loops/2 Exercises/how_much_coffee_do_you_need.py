command = input()

total_cups = 0

while command != "END":
    if command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie" \
            or command.lower() == "coding":
        if command.islower():
            total_cups += 1
        else:
            total_cups += 2
    command = input()

if total_cups <= 5:
    print(total_cups)
else:
    print("You need extra sleep")
