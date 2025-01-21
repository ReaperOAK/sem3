def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter a valid choice.")