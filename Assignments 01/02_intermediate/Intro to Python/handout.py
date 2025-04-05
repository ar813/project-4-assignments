print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturn")
print("6. Uranus")
print("7. Neptune")

weight_on_earth = float(input("Enter a weight on Earth (in kg): "))
planet = int(input("Choose the number for the planet above (1-7): "))

if planet == 1:
    weight_on_mercury = round(0.376 * weight_on_earth, 2)
    print(f"The weight on Mercury is {weight_on_mercury} kg")
elif planet == 2:
    weight_on_venus = round(0.889 * weight_on_earth, 2)
    print(f"The weight on Venus is {weight_on_venus} kg")
elif planet == 3:
    weight_on_mars = round(0.378 * weight_on_earth, 2)
    print(f"The weight on Mars is {weight_on_mars} kg")
elif planet == 4:
    weight_on_jupiter = round(2.360 * weight_on_earth, 2)
    print(f"The weight on Jupiter is {weight_on_jupiter} kg")
elif planet == 5:
    weight_on_saturn = round(1.081 * weight_on_earth, 2)
    print(f"The weight on Saturn is {weight_on_saturn} kg")
elif planet == 6:
    weight_on_uranus = round(0.815 * weight_on_earth, 2)
    print(f"The weight on Uranus is {weight_on_uranus} kg")
elif planet == 7:
    weight_on_neptune = round(1.140 * weight_on_earth, 2)
    print(f"The weight on Neptune is {weight_on_neptune} kg")
else:
    print("Invalid choice. Please select a number between 1 and 7.")
