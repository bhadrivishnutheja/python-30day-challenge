# Find min/max number

def get_numbers_from_user():
    numbers = []
    n = int(input("How many numbers? "))
    for i in range(n):
        num = float(input(f"Enter number {i + 1}:"))
        numbers.append(num)
    return numbers

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_second_larget(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    return None

if __name__ == "__main__":
    numbers = get_numbers_from_user()
    print(f"\n Numbers: {numbers}")
    print(f" Maximum: {find_maximum(numbers)}")
    print(f" Minimum: {find_minimum(numbers)}")
    print(f"Second Largest Number: {find_second_larget(numbers)}")
          