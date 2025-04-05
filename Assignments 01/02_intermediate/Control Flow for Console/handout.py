import random

score = 0 
current_round  = 1

print("\nWelcome to the High-Low Game!")
print("--------------------------------")


while True:
    print(f"\nRound {current_round }")

    your_number = int(input("What is your number: "))
    computer_number = random.randint(1,100)

    check = input("Do you think your number is higher (type higher) or lower (type lower) than the computer's? ")
    
    while check != "lower" and check != "higher":
        check = input("Please enter either 'higher' or 'lower': ")

    if check == "lower":
        if your_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    if check == "higher":
        if your_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}")    
    current_round  += 1
    
    if current_round  > 5:
        break