#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_val = my_list[0]  # Initialize max_val with the first element of the list
    for num in my_list:
        if num > max_val:
            max_val = num
    return max_val
