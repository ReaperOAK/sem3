def demonstrate_multiple_except_blocks():
    try:
        # Example operation that may raise different exceptions
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
demonstrate_multiple_except_blocks()