def count_even(lst):
    even_list = []
    count = 0
    for number in lst:
        if number % 2 == 0:
            count += 1
            even_list.append(number)
    print(even_list)
    print(count)

user_lst = []

while True:
    user_input = input("Enter an integer or press enter to stop: ")
    if user_input == "":
        break
    user_lst.append(int(user_input))

count_even(user_lst)
