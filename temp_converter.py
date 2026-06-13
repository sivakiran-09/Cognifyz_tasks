print("----Temperature Converter----")
print()

temperature = float(input("Enter the temperature value:"))

print("\n Choose the conversion direction:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice:")

if choice == '1':
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")

elif choice == '2':
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius:.2f}°C")

else:
    print("Invalid choice! Please choose either 1 or 2.")        