def separate_even_odd(input_list):
    even_list = []
    odd_list = []
    for number in input_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return even_list, odd_list

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Input list:", input_list)

even_list, odd_list = separate_even_odd(input_list)
print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)