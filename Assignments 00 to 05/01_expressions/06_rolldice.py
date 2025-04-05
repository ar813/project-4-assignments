import random

def main():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    print(f"🎲 Die1: {die1}, \n🎲 Die2: {die2}, \n➡️  Total: {total}")


if __name__ == '__main__':
    main()