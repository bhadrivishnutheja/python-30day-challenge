# Multiplication tables
def print_table(num, limit=10):
    print(f"\n --- Multiplication Table of {num} ---")
    for i in range(1, limit + 1):
        result = num * i
        print(f" {num} x {i} = {result}")
def print_mulitple_tables(start,end):
    for num in range(start, end + 1):
        print_table(num)
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    limit = int(input("Enter limit (default 10): ") or 10)
    print_table(num, limit)