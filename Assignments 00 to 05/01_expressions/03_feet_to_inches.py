def main():
    feet = float(input("Enter the length (feet): "))
    
    # 1 feet = 12 inches
    
    inch = feet * 12
    print(f"{feet} feet = {inch:.2f} inch")



if __name__ == '__main__':
    main()