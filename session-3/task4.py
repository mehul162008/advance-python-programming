my_list = [1, 2, 3]
my_dict = {'a': 1}

try:
    print(my_list[5])
    print(my_dict['b'])

except IndexError:
    print("Error: List index is out of range.")

except KeyError:
    print("Error: Dictionary key not found.")