
## **The Standard Project BludPrint**
```text
my_project/
│
├── my_module/            # The main folder for your Python code
│   ├── __init__.py       # Makes Python treat this folder as a package
│   ├── calculator.py     # Your logic/helper functions
│   └── app.py            # Your main entry point script
│
├── tests/                # Folder for your testing scripts
│   └── test_calculator.py
│
├── .gitignore            # Tells Git which files to ignore (like cache)
├── README.md             # Text file describing your project
└── requirements.txt      # List of external libraries needed
```


## **The Helper File**
```python
#caluculator.py
def add(a, b):
    return a + b

# This only runs if we run calculator.py directly
if __name__ == "__main__":
    print("Testing the calculator...")
    print(add(5, 5))

```

## **The Main File**
```python
# app.py
import calculator

print("This is the main applicaiton")
result=calculator.add(10,20)
print(f"Result: {result}")
```