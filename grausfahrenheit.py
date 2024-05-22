from math import ceil

fahrenheit = float(input("Digite a temperatura em fahrenheit: "))

celsius = (fahrenheit - 32)*5/9

celsius = ceil(celsius)

print(f"A temperatura em celsius e: {celsius:.2f}°c")