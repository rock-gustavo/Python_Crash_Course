
"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you
could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

"""

dream_vacations = {}

while True:
    name = input("What's your name? ").strip().lower()
    vacation = input("If you could visit one place in the world, where would you go? ").strip()
    dream_vacations[name] = vacation
    response = input("Do you think that someone else should take this pool[Y/N]?").strip().lower()[0]
    while response not in "yn":
        response = input("Do you think that someone else should take this pool[Y/N]?").strip().lower()[0]
    if response == 'n':
        break

for k, v in dream_vacations.items():
    print(f"\n{k.title()} dream vacation is: \n\t{v}")
print("\nFIM")