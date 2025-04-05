import random

NUM_SIDES = 6 # It is a global variable

def rolling_two_dice():
    random_number_one = random.randint(1,NUM_SIDES)
    random_number_two = random.randint(1,NUM_SIDES)
    total = random_number_one + random_number_two
    print(f"Total is {total}")

def main():
    random_number_one = 10 # It is a local variable
    rolling_two_dice()
    rolling_two_dice()
    rolling_two_dice()
    print(f"Random number one in main function is {random_number_one}")


if __name__ == '__main__':
    main()