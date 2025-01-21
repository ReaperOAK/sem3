def append_to_list(original_list, element):
    original_list.append(element)
    return original_list

# Example usage
my_list = [1, 2, 3]
print("Original list:", my_list)

element_to_add = 4
updated_list = append_to_list(my_list, element_to_add)
print("Updated list after appending:", updated_list)

element_to_add = 5
updated_list = append_to_list(my_list, element_to_add)
print("Updated list after appending:", updated_list)