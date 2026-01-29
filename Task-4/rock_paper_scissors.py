import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("Rock Paper Scissors Game")

while True:
    user = input("Choose rock/paper/scissors: ").lower()
    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("Tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win")
        user_score += 1
    else:
        print("You lose")
        computer_score += 1

    print("Score -> You:", user_score, "Computer:", computer_score)

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break

print("Final Score -> You:", user_score, "Computer:", computer_score)
