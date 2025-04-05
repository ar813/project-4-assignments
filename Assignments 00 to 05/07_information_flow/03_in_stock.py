def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    elif fruit == 'banana':
        return 4
    elif fruit == 'pear':
        return 1000
    else:
        return 0  # To handle fruits that are not in stock

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print(f"Number of {fruit}s in stock: {stock}")

if __name__ == '__main__':
    main()
