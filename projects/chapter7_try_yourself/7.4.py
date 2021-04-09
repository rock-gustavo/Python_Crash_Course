
"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit'
value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

"""

while True:
    topping = input("\nWhich topping that you want to add to your pizza(enter 'quit' to stop)? ")
    if topping == "quit":
        break
    else:
        print(f"We will add {topping} to your pizza.")
print("FIM")