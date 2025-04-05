num_tracking = {} # {"3":2}  3 appears 2 times

def main():
    
    while True:
        num = input("Enter a number (or 'q' to quit): ")
        
        if num.lower() == "q":
            break
        
        num = int(num)
        if num in num_tracking:
            num_tracking[num] += 1
        else:
            num_tracking[num] = 1
            
    for key, value in num_tracking.items():
        print(f"{key} appears {value} times.")


if __name__ == '__main__':
    main()