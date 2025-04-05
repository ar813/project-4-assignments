def get_lst():
    lst = []
    elements = input("Please enter an element of the list or write (q) to quit: ")
    while elements != "q":
        lst.append(elements)
        elements = input("Please enter an element of the list or write (q) to quit: ")
    return lst


def get_first_element(lst):
    first_element = lst[0]
    return first_element


def main():
    my_list = get_lst()
    func = get_first_element(my_list)
    print(func)
    
    
if __name__ == '__main__':
    main()