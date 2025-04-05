import random


def main():
    lst = []
    
    for i in range(10):
        random_num = random.randint(1,100)
        lst.append(random_num)
        
    print(lst)
    

    lst_string = " ".join(map(str, lst))  
    print(lst_string)
    
    # Explanation:
    # 1. map(str, lst) → Converts each number in the list to a string
    # 2. " ".join(...) → Joins all string numbers with a space

    


if __name__ == '__main__':
    main()