# Leap Year checker
def  is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def get_days_in_february(year):
    if is_leap_year(year):
        return 29
    else:
        return 28

def display_leap_year(year):
    if is_leap_year(year):
        print(f"{year} is a Leap Year! ")
        print(f" Feb has {get_days_in_february(year)} days.")
    else:
        print(f"{year} is not a Leap year! ")
        print(f" February has {get_days_in_february(year)} days.")
if __name__ == "__main__":
    year = int(input("Enter a year: "))
    display_leap_year(year)