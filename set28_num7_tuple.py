# Task 1: Display numbers divisible by 7 but not a multiple of 5, between 1000 and 2000
def find_numbers():
    result = []
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            result.append(num)
    return result

# Task 2: Display the first half and last half values of a tuple in separate lines
def display_tuple_halves(t):
    half = len(t) // 2
    first_half = t[:half]
    last_half = t[half:]
    return first_half, last_half

# Task 1
numbers = find_numbers()
print("Numbers divisible by 7 but not a multiple of 5, between 1000 and 2000:")
print(numbers)

# Task 2
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_half, last_half = display_tuple_halves(t)
print("First half of the tuple:")
print(first_half)
print("Last half of the tuple:")
print(last_half)