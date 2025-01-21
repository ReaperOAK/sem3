# Function to reverse a string without using built-in functions
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Function to convert a dictionary to a list of tuples and sort it
def dict_to_sorted_tuples(d):
    tuple_list = [(k, v) for k, v in d.items()]
    return sorted(tuple_list)

# Example usage for reversing a string
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")

# Example usage for converting dictionary to sorted list of tuples
original_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_tuples = dict_to_sorted_tuples(original_dict)
print(f"Original dictionary: {original_dict}")
print(f"Sorted list of tuples: {sorted_tuples}")