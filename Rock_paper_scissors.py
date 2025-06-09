import random

def play_game(rounds=3):
    choices = ['Rock', 'Paper', 'Scissors']
    user_points = 0
    computer_points = 0
    valid_rounds = 0

    while valid_rounds < rounds:
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        
        # Validate input
        if not user_choice:
            print("Empty input! Please enter Rock, Paper, or Scissors.")
            continue
        if user_choice not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        # Computer's choice
        computer_choice = random.choice(choices)
        
        # Display choices
        print(f"You chose {user_choice}, Computer chose {computer_choice}")

        # Determine outcome
        if user_choice == computer_choice:
            print("It's a tie! No points awarded.")
        elif (user_choice, computer_choice) in [("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")]:
            print("You win this round!")
            user_points += 1
        else:
            print("Computer wins this round!")
            computer_points += 1

        valid_rounds += 1
        print(f"Score - You: {user_points}, Computer: {computer_points}\n")

    # Declare winner
    if user_points > computer_points:
        print(f"You won the game! Final Score - You: {user_points}, Computer: {computer_points}")
    elif computer_points > user_points:
        print(f"Computer won the game! Final Score - You: {user_points}, Computer: {computer_points}")
    else:
        print(f"It's a tie! Final Score - You: {user_points}, Computer: {computer_points}")

# Main loop for replay
while True:
    play_game(rounds=3)
    replay = input("Play again? (yes/no): ").lower()
    if replay != 'yes':
        print("Thanks for playing!")
        break