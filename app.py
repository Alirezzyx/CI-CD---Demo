import random
import os


os.system('cls')

choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

user_score = 0
computer_score = 0

print("🎮 Rock, Paper, Scissors Game")
print("First player to win 3 rounds is the winner.\n")

while user_score < 3 and computer_score < 3:
    print("Choose one:")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")

    try:
        user_choice = int(input("Your choice (1/2/3): "))
        if user_choice not in [1, 2, 3]:
            print("❌ Please enter only 1, 2, or 3!\n")
            continue
    except ValueError:
        print("❌ Please enter a number!\n")
        continue

    computer_choice = random.randint(1, 3)

    print(f"👤 You chose: {choices[user_choice]}")
    print(f"💻 Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!\n")
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        user_score += 1
        print("✅ You win this round!\n")
    else:
        computer_score += 1
        print("❌ Computer wins this round!\n")

    print(f"📊 Score → You: {user_score} | Computer: {computer_score}")
    print("-" * 30)

if user_score == 3:
    print("Congratulations! You won the game!")
else:
    print("Computer won the game!")