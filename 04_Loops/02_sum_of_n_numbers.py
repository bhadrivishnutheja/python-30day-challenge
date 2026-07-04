# sum of n numbers
def sum_using_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_using_formula(n):
    return n * (n + 1 ) // 2
def sum_of_even(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total
def sum_of_odd(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i
    return total
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f" Sum of first {n} numbers using (loop): {sum_using_loop(n)}")
    print(f" Sum of first {n} numbers (formula): {sum_using_formula(n)}")
    print(f" Sum of even number up to {n}: {sum_of_even(n)}")
    print(f" Sum of odd numbers up to {n}: {sum_of_odd(n)}")
