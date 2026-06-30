def celcius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def fahrenheit_to_celcius(temp):
    return (temp - 32) * 5/9

def convert_temperature(temp, units):
    if units == "C":
        result = celcius_to_fahrenheit(temp)
        return f"{temp}C is equal to {result}F"
    elif units == "F":
        result = fahrenheit_to_celcius(temp)
        return f"{temp}F is equal to {result}C"
    else:
        return "invalid Unit input"
if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    units = input("Enter units (C or F): ").upper()
    result = convert_temperature(temp, units)
    print(f"Converted temperature: {result} {'F' if units == 'C' else 'C'}")

