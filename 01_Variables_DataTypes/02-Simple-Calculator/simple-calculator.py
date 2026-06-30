def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
def calcuator(num1, num2, operator):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "*":
        return mul(num1, num2)
    elif operator == "/":
        return div(num1, num2)
    else:
        return "Invalid operator"

if __name__ == "__main__":
    num1 = float(input("Enter fist number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    result = calcuator(num1, num2, operator)
    print(f" Result: {result}")