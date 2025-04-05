phonebook = {}

while True:
    print("\n1. Add\n2. Display\n3. Search\n4. Exit")
        
    choice = int(input("\nPlease select one of them: "))

    if choice == 1:
        name = input("Enter your name: ")
        number = int(input("Enter your phone number: "))
        
        phonebook[name] = number  # Store in dictionary
        print(f"{name} added successfully!")
        
    elif choice == 2:
        for name, number in phonebook.items(): # name = key; number = value
            print(f"{name} --> {number}")
            
    elif choice == 3:
        search_name  = input("Enter the name to search: ")
        
        if search_name  in phonebook:
                print(f"{search_name} --> {phonebook[search_name]}")
        else:
            print("No number found!")
    
    elif choice == 4:
        print("Good Bye... 👋")
        break
    
    else:
        print("Invalid choice, please enter a number between 1-4.")