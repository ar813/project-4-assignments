def main():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))
    
    if num2 == 0: 
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        remainder = num1 % num2
        print(f"The result of this division is {result} with a remainder of {remainder}")

    
if __name__ == '__main__':
    main()