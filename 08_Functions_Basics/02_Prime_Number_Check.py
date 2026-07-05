# Check the Prime Number 
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def next_prime(number):
    num = number + 1
    while not is_prime(num):
        num += 1
    return num

def count_primes(start, end):
    return len(primes_in_range(start, end))

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a Prime Number ")
    else:
        print(f"{num} is not a Prime Number ")

    start = int(input("\n Enter start of range: "))
    end = int(input("Enter end of range: "))
    primes = primes_in_range(start, end)
    print(f"Primes between {start} and {end}: {primes}")
    print(f"Total primes: {count_primes(start, end)}")
    print(f"Next prime after {num}: {next_prime(num)}")