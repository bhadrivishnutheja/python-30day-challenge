# odd/Even Checker
def check_add_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def check_divisiblity(number):
    divisible_by = []
    for i in [3, 5, 7]:
        if number % i == 0:
            divisible_by.append(i)
    return divisible_by
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    retsult = check_add_even(num)
    print(f"{num} is {retsult}.")

    divisilbe = check_divisiblity(num)
    if divisilbe:
        print(f"Also divisilbe by: {divisilbe}")