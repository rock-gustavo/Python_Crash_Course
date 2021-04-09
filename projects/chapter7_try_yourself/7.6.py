
"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least
once: Use a conditional test in the while statement to stop the loop. Use an active variable to control how long the
loop runs. Use a break statement to exit the loop when the user enters a 'quit' value.

"""
x = 0

while x <= 5:
    topping = input("\nWhich topping that you want to add to your pizza(enter 'quit' to stop)? ")
    if topping == "quit":
        break
    else:
        print(f"We will add {topping} to your pizza.")
        x += 1

print("FIM")