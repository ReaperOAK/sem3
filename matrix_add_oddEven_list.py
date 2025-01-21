def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def separate_odd_even(numbers):
    odd_list = []
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return odd_list, even_list

# Example matrices for addition
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Example list for separating odd and even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Perform matrix addition
result_matrix = add_matrices(matrix1, matrix2)
print("Result of matrix addition:")
for row in result_matrix:
    print(row)

# Separate odd and even numbers
odd_list, even_list = separate_odd_even(numbers)
print(f"Odd numbers: {odd_list}")
print(f"Even numbers: {even_list}")