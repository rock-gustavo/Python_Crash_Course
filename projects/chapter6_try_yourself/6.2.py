"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in
your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each
person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your
program.
"""

fav_number = {'gustavo': 11, 'clara': 7, 'enzo': 8}

for k, v in fav_number.items():
    print(f"{k.title()}'s favorite number is {v}")
print('FIM')