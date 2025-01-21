# Function to invert keys and values in a dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}

# Function to find the frequency of occurrence of numbers in a given list
def frequency_of_numbers(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Example usage for inverting dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(original_dict)
print(f"Original dictionary: {original_dict}")
print(f"Inverted dictionary: {inverted_dict}")

# Example usage for frequency of numbers
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = frequency_of_numbers(numbers)
print(f"Frequency of numbers in the list: {frequency}")