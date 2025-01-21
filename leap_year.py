def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0

# Example usage
year = int(input("Enter a year: "))
result = is_leap_year(year)
if result == 1:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")