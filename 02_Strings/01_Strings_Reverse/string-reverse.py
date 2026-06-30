# String Reverse
#method 1: Using slicing
def reverse_string_slice(original_string):
    return original_string[::-1]
# method 2: Using a loop
def reverse_string_iterator(text:str ) -> str:
    return "".join(reversed(text))
if __name__ == "__main__":
    original_string = input("Enter a string to reverse: ")
    reversed_slice = reverse_string_slice(original_string)
    print(f"Original String: {original_string}")
    print(f"Reversed String using slicing: {reversed_slice}")

    reversed_iterator = reverse_string_iterator(original_string)
    print(f"Reversed String using iterator: {reversed_iterator}")