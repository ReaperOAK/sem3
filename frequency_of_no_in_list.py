def frequency_of_numbers(input_list):
    frequency_dict = {}
    for number in input_list:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1
    return frequency_dict

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print("Input list:", input_list)

frequency_dict = frequency_of_numbers(input_list)
print("Frequency of numbers:", frequency_dict)