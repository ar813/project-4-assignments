def main():
    age = int(input("\nHow old are you? "))

    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16 to 24.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16 to 24")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25 to 47.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25 to 47.")

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48 to above.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48 to above.")

if __name__ == '__main__':
    main()
