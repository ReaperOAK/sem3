def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    return sum(num for num in numbers if is_prime(num))

def get_day_of_week(number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 1 <= number <= 7:
        return days[number - 1]
    else:
        return "Invalid number. Please enter a number between 1 and 7."

# Example usage for sum of prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
sum_primes = sum_of_primes(prime_numbers)
print(f"The sum of the list of prime numbers is: {sum_primes}")

# Example usage for getting the relevant day of the week
number = int(input("Enter a number (1-7) to get the relevant day of the week: "))
day = get_day_of_week(number)
print(f"The relevant day for number {number} is: {day}")