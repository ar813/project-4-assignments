def computer_guess_number():
    print("\nPlease think of a number between 1 and 100, and I'll try to guess it.")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    feedback = ''

    while feedback != 'c':
        guess = (low + high) // 2  # Computer's guess
        feedback = input(f"Is your number {guess}? (Enter 'h' for too high, 'l' for too low, 'c' for correct): ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number, {guess}!")
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guess_number()