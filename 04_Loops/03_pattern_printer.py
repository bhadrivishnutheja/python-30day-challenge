# Pattern Printer
def right_triangle(rows):
    print("\n --- Right Triangle ---")
    for i in range(1, rows + 1):
        print("*" * i)

def inverted_triangle(rows):
    print("\n --- inverted triangle ---")
    for i in range(rows, 0, -1):
        print("*" * i)

def pyramid(rows):
    print("\n --- Pyramid ---")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        starts = "*" * (2 * i - 1)
        print(spaces + starts)

def number_pattern(rows):
    print("\n --- Number Pattern ---")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    right_triangle(rows)
    inverted_triangle(rows)
    pyramid(rows)
    number_pattern(rows)

