MAX_LENGTH: int = 3

def shorten(lst):
    print("")
    while len(lst) > MAX_LENGTH:
        elements = lst.pop()
        print(f"{elements} has removed")
    print("\nFinal list:", lst)

def main():
    my_list = [1, 2, 3, 4, 5, "one", "two", "three", "four", "five"]
    shorten(my_list)


if __name__ == '__main__':
    main()