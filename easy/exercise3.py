# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

def get_first_last(a):
    new_list = [a[0], a[-1]]
    return new_list

a = [5, 10, 15, 20, 25]

result = get_first_last(a)

print(result)