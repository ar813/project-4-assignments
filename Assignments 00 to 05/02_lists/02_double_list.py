def doubling_the_numbers(list_of_numbers):
    doubled_list = []
    
    for number in list_of_numbers:
        value  = number  * 2
        doubled_list.append(value)
        
    return doubled_list 

def main():
    result  = doubling_the_numbers([1,2,3])
    print(f"Doubled List: {result}")

if __name__ == '__main__':
    main()