# program 1: Hello World + User Greetings
def greet_user():
    print("Hello, World!")
    name = input("What is your name? ")
    age = input("What is your age? ")
    print(f"Hello, {name}! Welcome!")
    print(f"You are {age} years old.")
    print(f"Nice to meet you {name}!")
    return name, age

if __name__ == "__main__":
    greet_user()