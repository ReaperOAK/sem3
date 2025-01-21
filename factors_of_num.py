def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number to find its factors: "))
factors = find_factors(number)
print(f"The factors of {number} are: {factors}")