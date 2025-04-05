fruits = {
    "apple": 50,
    "banana": 60,
    "watermelon": 75,
    "strawberry": 90,
    "mango": 100
}

total_cost = 0

for fruit, price in fruits.items():
    quantity = int(input(f"How many {fruit}s do you want? "))  
    total_cost += quantity * price 

print("\nYour total cost is: $", total_cost)