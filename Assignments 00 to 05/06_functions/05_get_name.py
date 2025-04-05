def get_name(name):
    return name

def main():
    user_name = input("Enter your name: ").title()
    name = get_name(user_name)
    print("Howdy", name, "! 🤠")
    
if __name__ == "__main__":
    main()
