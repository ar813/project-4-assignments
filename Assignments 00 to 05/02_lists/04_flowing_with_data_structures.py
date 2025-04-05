# Immutable (Number)
def change_number(x):
    x = x + 10 
    return x

num = 5
new_num = change_number(num)
print(num)      # Output: 5 (unchanged because it has a fixed value)
print(new_num)  # Output: 15 (changed because we returned it)

# Mutable (List)
def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)
    # No need to return anything

my_list = []
add_three_copies(my_list, "Hello World!")
print(my_list)  # Output: ['Hello World!', 'Hello World!', 'Hello World!'] (list is changed!)