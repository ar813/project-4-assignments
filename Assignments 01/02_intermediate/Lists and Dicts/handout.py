def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("\nInitial fruit list:", fruit_list)
    print("Length of the list:", len(fruit_list))
    fruit_list.append("mango")
    print("Updated fruit list:", fruit_list)

def access(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def modify(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    lst[index] = new_value
    return lst

def slice(lst, start_index, last_index):
    new_lst = lst[start_index:last_index]
    return new_lst

def game_interaction():
    lst = [1, "Cat", 2, "Dog", 3]  # Sample list for the game
    
    print("\nWelcome to the list manipulation game!")
    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice the list")
        print("4. Quit the game")
        
        operation = input("Enter the operation number: ").strip()
        
        if operation == "1":  # Access an element
            index = int(input("Enter the index to access: "))
            result = access(lst, index)
            print(f"Result: {result}")
        
        elif operation == "2":  # Modify an element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify(lst, index, new_value)
            print(f"Updated list: {result}")
        
        elif operation == "3":  # Slice the list
            start_index = int(input("Enter the start index for slicing: "))
            last_index = int(input("Enter the last index for slicing: "))
            result = slice(lst, start_index, last_index)
            print(f"Sliced list: {result}")
        
        elif operation == "4":  # Quit the game
            print("\nThanks for playing!")
            break
        
        else:
            print("Invalid input, please choose a valid operation number.")

main()
game_interaction()
