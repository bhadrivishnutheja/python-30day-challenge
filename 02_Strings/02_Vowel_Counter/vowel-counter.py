# Vowel Counter
from pydoc import text


def show_vowels_count(user_string):
    vowels = "aeiouAEIOU"
    found_vowels = [ char for char in user_string if char in vowels]
    print(f" Vowels found: {''.join(found_vowels)}")
    print(f" Total number of vowels found: {len(found_vowels)}")
if __name__ == "__main__":
    count_string = input("enter a string to count vowels: ")
    show_vowels_count(count_string)
