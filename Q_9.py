temp = float(input("Enter Temperature: "))
unit = input("Enter unit ('C' for Celsius or 'F' for Fahrenheit): ").strip().lower()

if unit == 'c':
    new_temp = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit = {round(new_temp, 2)}°F")
elif unit == 'f':
    new_temp = (temp - 32) * 5/9
    print(f"Temperature in Celsius = {round(new_temp, 2)}°C")
else:
    print("Unknown unit:", unit)
