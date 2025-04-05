def odd(lst):
    odd_lst = []
    even_lst = []
    for number in lst:
        if number % 2 != 0:
           odd_lst.append(f"{number} is Odd.")
        else:
            even_lst.append(f"{number} is Even.")
    
    odd_numbers = ""
    for num in odd_lst:
        odd_numbers += str(num) + "\n" 

    even_numbers = ""
    for num in even_lst:
        even_numbers += str(num) + "\n"
    
    print(even_numbers)
    print(odd_numbers)
            

def main():
    odd([11,12,13,14,15,16,17,18,19,20])

if __name__ == '__main__':
    main()