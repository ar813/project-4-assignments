AFFIRMATION : str = "I believe in myself."

def main():
    print("\nPlease type the following affirmation: " + AFFIRMATION)
    
    user_feedback = input() 
    while user_feedback != AFFIRMATION: 
        print("That was not the affirmation.")

        print("\nPlease type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")


if __name__ == '__main__':
    main()