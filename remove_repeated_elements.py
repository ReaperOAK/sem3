def remove_repeated_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", input_list)
unique_list = remove_repeated_elements(input_list)
print("List after removing repeated elements:", unique_list)