import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("\nWelcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

if __name__ == "__main__":
    play_game()
