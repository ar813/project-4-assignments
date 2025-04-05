def greet(name):
    return f"Greetings {name}!"

def main():
    name = input("What's your name? ")
    func = greet(name)
    print(func)

if __name__ == '__main__':
    main()