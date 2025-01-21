def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
series = fibonacci_series(num_terms)
print("Fibonacci series:", series)