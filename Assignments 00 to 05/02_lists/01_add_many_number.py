def add_numbers(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total

def add_numbers_by_built_in_function(list_of_numbers):
    return sum(list_of_numbers)

def main():
    total  = add_numbers([1,2,3,4,5,6,7,8,9])
    total_builtin   = add_numbers_by_built_in_function([1,2,3,4,5,6,7,8,9])
    
    print(f"Sum (manual loop): {total}")
    print(f"Sum (built-in function): {total_builtin}")


if __name__ == '__main__':
    main()