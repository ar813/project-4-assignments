def main():
    mass = int(input("Enter the mass (kg): "))   
    SPEED_OF_LIGHT = 299792458
    energy = mass * SPEED_OF_LIGHT**2
    
    print(f"Energy = {energy:.2f} joules (J)")

if __name__ == '__main__':
    main()