def modulus_complex(c):
    return abs(c)

def conjugate_complex(c):
    return c.conjugate()

# Example usage
real_part = float(input("Enter the real part of the complex number: "))
imaginary_part = float(input("Enter the imaginary part of the complex number: "))
complex_number = complex(real_part, imaginary_part)

modulus = modulus_complex(complex_number)
conjugate = conjugate_complex(complex_number)

print(f"The modulus of the complex number {complex_number} is: {modulus}")
print(f"The conjugate of the complex number {complex_number} is: {conjugate}")