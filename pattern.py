# Function to print star pattern
def star_pattern(n):
    for i in range(1, n + 1):
        print('⭐' * i)

# Function to print number pattern
def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

# Function to print continuous number pattern
def continuous_number_pattern(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

# Example usage
n = 5
print("Star Pattern:")
star_pattern(n)

print("\nNumber Pattern:")
number_pattern(n)

print("\nContinuous Number Pattern:")
continuous_number_pattern(n)