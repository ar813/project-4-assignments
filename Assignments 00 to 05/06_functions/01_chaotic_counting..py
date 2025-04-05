import random

def done():
    true_or_false = random.choice([True, False])
    return true_or_false

def chaotic_counting():
    for i in range(1, 11): # 1 to 10
        if done():
            return # this ends the function execution, so we'll get back to the main() function!
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == '__main__':
    main()