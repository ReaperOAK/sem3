def find_max_min(a, b, c):
    maximum = max(a, b, c)
    minimum = min(a, b, c)
    return maximum, minimum

# Example usage
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

maximum, minimum = find_max_min(a, b, c)
print(f"The maximum of the three numbers is: {maximum}")
print(f"The minimum of the three numbers is: {minimum}")