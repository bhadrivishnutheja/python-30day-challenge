# Grade Calculator
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >=80:
        return 'B'
    elif marks >=70:
        return 'C'
    elif marks >=60:
        return 'D'
    else:
        return 'F'

def display_results(marks, grade):
    print(f"\n Marks: {marks}")
    print(f" Grade: {grade}")
    if grade in ['A', 'B']:
        print("Excellent! Keep it up!")
    elif grade == 'C':
        print("Good! you can do better!")
    elif grade == 'D':
        print("Need improvement!")
    else:
        print("Failed! Work Hard !!!!")
if __name__ == "__main__":
    marks = float(input("Enter marks (0-100): "))
    if 0 <= marks <= 100:
        grade = calculate_grade(marks)
        display_results(marks, grade)
    else:
        print("Invalid marks. enter between 0 to 100.")
