
"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

"""

number = int(input("Choose an integer number: "))
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10")
else:
    print(f"The number {number} is not a multiple of 10.")
