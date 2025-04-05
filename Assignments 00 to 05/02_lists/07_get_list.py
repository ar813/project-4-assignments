def get_lst():
    lst = []
    elements = input("Enter a value: ")
    while elements != "":
        lst.append(elements)
        elements = input("Enter a value: ")
    return lst

def main():
    my_list = get_lst()
    print(my_list)
    
    
if __name__ == '__main__':
    main()