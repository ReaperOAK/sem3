import cmath

def find_roots(a, b, c):
    try:
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
        
        # Calculate the discriminant
        discriminant = b**2 - 4*a*c
        
        # Calculate the two roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        
        return root1, root2
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    roots = find_roots(a, b, c)
    if isinstance(roots, tuple):
        print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")
    else:
        print(roots)
except ValueError:
    print("Invalid input. Please enter numeric values for the coefficients.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")