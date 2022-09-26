import random

players_choice = input("Choose[r]ock, [p]aper, [s]cissors: ")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_choice = ""

if players_choice == "r":
    players_choice = rock
elif players_choice == "p":
    players_choice = paper
elif players_choice == "s":
    players_choice = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random_choice = random.randint(1, 3)
if computer_random_choice == 1:
    computer_choice = rock
elif computer_random_choice == 2:
    computer_choice = paper
else:
    computer_choice = scissors

print(f"The computer chose {computer_choice}.")

if (players_choice == rock and computer_choice == scissors) or \
        (players_choice == paper and computer_choice == rock) or \
        (players_choice == scissors and computer_choice == paper):
    print("You win")
elif (players_choice == rock and computer_choice == paper) or \
        (players_choice == paper and computer_choice == scissors) \
        or (players_choice == scissors and computer_choice == rock):
    print("You lose")
else:
    print("Draw")
