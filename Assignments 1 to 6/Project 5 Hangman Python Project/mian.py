import random

def choose_word():
    """Selects a random word from a predefined list."""
    words = ['python', 'hangman', 'programming', 'developer', 'challenge']
    return random.choice(words)

def display_progress(word, guessed_letters):
    """Displays the current progress of the word with guessed letters revealed."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    """Main function to play the Hangman game."""
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("\nWelcome to Hangman!")
    print("Try to guess the word, one letter at a time.")

    while attempts > 0:
        print("\n" + display_progress(word_to_guess, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")

        all_guessed = True
        for letter in word_to_guess:
            if letter not in guessed_letters:
                all_guessed = False
                break

        if all_guessed:
            print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nGame over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
