# Area Calculator
import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side ** 2

def area_trapezoid(a, b, height):
    return 0.5 * (a + b) * height

def perimeter_circle(radius):
    return 2 * math.pi * radius

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def display_menu():
    print("\n ======= Area Calculator ======")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Trapezoid")
    print("6. Perimeter")

def calculate_area(choice):
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = area_circle(radius)
        print(f"Area of the circle: {area:.2f}")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_rectangle(length, width)
        print(f"Area of the rectangle: {area:.2f}")
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_triangle(base, height)
        print(f"Area of the triangle: {area:.2f}")
    elif choice == '4':
        side = float(input("Enter the side of the square: "))
        area = area_square(side)
        print(f"Area of the square: {area:.2f}")
    elif choice == '5':
        a = float(input("Enter the first parallel side of the trapezoid: "))
        b = float(input("Enter the second parallel side of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        area = area_trapezoid(a, b, height)
        print(f"Area of the trapezoid: {area:.2f}")
    elif choice == '6':
        radius = float(input("Enter the radius of the circle: "))
        perimeter = perimeter_circle(radius)
        print(f"Perimeter of the circle: {perimeter:.2f}")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    display_menu()
    choice = input("Enter choice (1-6): ")
    calculate_area(choice)