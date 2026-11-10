
# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and 
# returns (then prints) an appropriate boolean.


def check_list(l, z):
    if z in l:
        return True
    else:
        return False

numbers = [1, 3, 5, 7, 9]

print(check_list(numbers, 5))