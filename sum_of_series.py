import math

def sum_of_series(n):
    total_sum = 0
    for i in range(1, n + 1):
        term = (i ** i) / math.factorial(i)
        total_sum += term
    return total_sum

n = int(input("Enter the value of n: "))
result = sum_of_series(n)
print(f"The sum of the series up to {n} is: {result}")