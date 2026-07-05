#  Function Calculator
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mulitiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b
def power(a, b):
    return a ** b

def get_operation(choice, a, b):
    operations = {
        '1': add, 
        '2': sub,
        '3': mulitiply,
        '4': divide,
        '5': modulus,
        '6': power
    }
    if choice in operations:
        return operations[choice](a, b)
    return "Invalid choice"

def display_menu():
    print("\n ----- Calculator Menu ------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")

if __name__ == "__main__":
    display_menu()
    choice = input("Enter choice (1-6): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = get_operation(choice, num1, num2)
    print(f"Reuslt: {result}")