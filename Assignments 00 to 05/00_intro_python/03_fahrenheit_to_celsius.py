def main():
    
    temperature_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5.0/9.0
    
    print(f"Temperature: {temperature_in_fahrenheit:.2f}°F = {temperature_in_celsius:.2f}°C")



if __name__ == '__main__':
    main()