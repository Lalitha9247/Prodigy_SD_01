def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def main():
    print("Temperature Conversion Program")
    print("Available temperature units: Celsius, Fahrenheit, Kelvin")
    
    original_unit = input("Enter the original temperature unit (C/F/K): ").upper()
    temperature = float(input("Enter the temperature value: "))
    
    if original_unit == "C":
        celsius = temperature
    elif original_unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
    elif original_unit == "K":
        celsius = kelvin_to_celsius(temperature)
    else:
        print("Invalid unit choice!")
        return
    
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    
    print(f"{temperature:.2f} {original_unit} is equal to:")
    print(f"{fahrenheit:.2f} F")
    print(f"{kelvin:.2f} K")

if __name__ == "__main__":
    main()
