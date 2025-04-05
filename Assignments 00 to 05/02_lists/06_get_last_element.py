def get_lst():
    lst = []
    elements = input("Please enter an element of the list or write (q) to quit: ")
    while elements != "q":
        lst.append(elements)
        elements = input("Please enter an element of the list or write (q) to quit: ")
    return lst


def get_last_element(lst):
    first_element = lst[-1]
    return first_element


def main():
    my_list = get_lst()
    func = get_last_element(my_list)
    print(func)
    
    
if __name__ == '__main__':
    main()