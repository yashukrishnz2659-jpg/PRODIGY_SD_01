

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def main():
    print("=== Temperature Conversion Program ===")
    print("Units: C for Celsius, F for Fahrenheit, K for Kelvin")

    try:
        temperature = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C/F/K): ").strip().upper()

        if unit == "C":
            f = celsius_to_fahrenheit(temperature)
            k = celsius_to_kelvin(temperature)
            print(f"\n{temperature}°C = {f:.2f}°F")
            print(f"{temperature}°C = {k:.2f}K")

        elif unit == "F":
            c = fahrenheit_to_celsius(temperature)
            k = fahrenheit_to_kelvin(temperature)
            print(f"\n{temperature}°F = {c:.2f}°C")
            print(f"{temperature}°F = {k:.2f}K")

        elif unit == "K":
            c = kelvin_to_celsius(temperature)
            f = kelvin_to_fahrenheit(temperature)
            print(f"\n{temperature}K = {c:.2f}°C")
            print(f"{temperature}K = {f:.2f}°F")

        else:
            print("Invalid unit! Please enter C, F, or K.")

    except ValueError:
        print("Invalid input! Please enter a numeric temperature value.")


if __name__ == "__main__":
    main()
