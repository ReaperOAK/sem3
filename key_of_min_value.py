def key_of_min_value(input_dict):
    if not input_dict:
        return None
    min_key = min(input_dict, key=input_dict.get)
    return min_key

# Example usage
input_dict = {'a': 10, 'b': 5, 'c': 8, 'd': 3}
print("Input dictionary:", input_dict)

min_key = key_of_min_value(input_dict)
print(f"The key of the minimum value is: {min_key}")