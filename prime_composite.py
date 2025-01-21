def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_prime_or_composite(number):
    if number <= 1:
        return "neither prime nor composite"
    elif is_prime(number):
        return "prime"
    else:
        return "composite"

# Example usage
num = int(input("Enter a number: "))
result = check_prime_or_composite(num)
print(f"{num} is {result}.")