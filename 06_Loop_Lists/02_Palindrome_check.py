# Palindrome Check !!! ?
def is_palindrome_string(text):
    cleaned = text.lower().replace(" ","")
    return cleaned == cleaned[::-1]

def is_palindrome_loop(text):
    cleaned = text.lower().replaced(" ","")
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_number(number):
    original = number
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10
    return original == reversed_num

def find_palindromes_in_list(words):
    palindromes = []
    for word in words:
        if is_palindrome_string(word):
            palindromes.append(word)
    return palindromes

if __name__ == "__main__":
    text = input("Enter a word or phrser: ")
    if is_palindrome_string(text):
        print(f" '{text}' is a Palindrome")
    else:
        print(f" '{text}' is NOT a Palindrome. ")

    num = int(input("\nEnter a Number: "))
    if is_palindrome_number(num):
        print(f"{num} is a Palindrome Number .")
    else:
        print(f"{num} is NOT a Palindrome.")

    words = ["madam", "hello", "level", "Python", "radar", "world"]
    print(f"\nWords: {words}")
    print(f"Palindromes: {find_palindromes_in_list(words)}")