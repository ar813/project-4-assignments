import random

random_number = random.randint(1, 6)
count = 0


while count < 3:
    guess_number = int(input("\nGuess the number between 1 to 6: "))
    
    if random_number == guess_number:
        print(f"🎉 Congrats! The number was:{random_number}")
        break
    elif random_number > guess_number:
        print("⬇️ You are too low... Try again!")    
    elif random_number < guess_number:
        print("⬆️ You are too high... Try again!")

    count += 1 

if count == 3 and guess_number != random_number:
    print(f"❌ Sorry! You've used all your attempts. The correct number was {random_number}.")