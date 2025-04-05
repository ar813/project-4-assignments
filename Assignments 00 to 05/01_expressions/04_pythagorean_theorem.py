import math

def main():
    base = float(input("Enter the length of the base: "))
    perpendicular = float(input("Enter the length of the perpendicular: "))
    calculation = (base**2) + (perpendicular**2)
    hypotenuse = math.sqrt(calculation)
    
    print(f"The length of hypotenuse is: {hypotenuse:.2f}")


if __name__ == '__main__':
    main()