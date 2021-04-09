"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the
kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

pet1 = {'animal': 'dog', 'owner': 'gustavo'}
pet2 = {'animal': 'dog', 'owner': 'clara'}
pet3 = {'animal': 'lizard', 'owner': 'gabi'}
pet4 = {'animal': 'fish', 'owner': 'enzo'}
pets = [pet1, pet2, pet3, pet4]

for c in pets:
    print(f'\nAnimal : {c["animal"]}')
    print(f'\tOwner: {c["owner"].title()}')
print('FIM')