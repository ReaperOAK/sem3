def add_complex(c1, c2):
    return c1 + c2

def subtract_complex(c1, c2):
    return c1 - c2

def multiply_complex(c1, c2):
    return c1 * c2

def divide_complex(c1, c2):
    return c1 / c2

# Example usage
c1 = complex(input("Enter the first complex number (e.g., 1+2j): "))
c2 = complex(input("Enter the second complex number (e.g., 3+4j): "))

print(f"Addition: {add_complex(c1, c2)}")
print(f"Subtraction: {subtract_complex(c1, c2)}")
print(f"Multiplication: {multiply_complex(c1, c2)}")
print(f"Division: {divide_complex(c1, c2)}")