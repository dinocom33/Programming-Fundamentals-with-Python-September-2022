import random

computer_number = random.randint(1, 100)

while True:
    player_guess = input("Guess the number (1-100): ")
    if not player_guess.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_guess)
    if player_number == computer_number:
        print("You guess it!")
        break
    elif player_number < computer_number:
        print("Too Small")
    else:
        print("Too High")
