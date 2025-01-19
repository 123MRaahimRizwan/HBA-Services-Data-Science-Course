# =============== IF CONDITIONS ===============

# Checking whether the number is greater than 5
number = int(input("Enter a number: "))

if number > 5:
    print("Number is greater than 5.")
elif number < 5:
    print("Number is lesser than 5.")
else:
    print("Enter a valid number.")

"""
Syntax:
if condition:
    code
elif condition:
    code
else:
    code
"""


# Whether is sunny or not
temperature = int(input("Enter the temperature in Celsius: "))

if temperature > 30:
    print("Weather is hot.")
elif temperature < 30:
    print("Weather is cold.")
else:
    print("Enter a valid temperature.")

"""
Talk about operators in IDLE :)
"""

# Food Dishes Example
pakistani = ["karahi", "qorma", "samosa"]
indian = ["dosa", "vada pav", "dhokla"]
portuguese = ["Francesinha", "Bolinhos de Bacalhau", "Carne de Porco à Alentejana"]

dish = input("Enter a dish name: ")

if dish in pakistani:
    print(f"{dish} is Pakistani.")
elif dish in indian:
    print(f"{dish} is indian.")
elif dish in portuguese:
    print(f"{dish} is portuguese.")
else:
    print("I don't know which dish you're asking for.")