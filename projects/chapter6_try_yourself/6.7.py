"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing
different people, and store all three dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person1 = {'first_name': 'clara', 'last_name': 'santos', 'age': 29, 'city': 'brasilia'}
person2 = {'first_name': 'gustavo', 'last_name': 'rocha', 'age': 36, 'city': 'brasilia'}
person3 = {'first_name': 'enzo', 'last_name': 'rocha', 'age': 9, 'city': 'brasilia'}
people = [person1, person2, person3]


for k in people:
    print(f' Full name: {k["first_name"].title()} {k["last_name"].title()}')
    print(f'\tAge: {k["age"]}')
    print(f'\tCity: {k["city"].title()}')
print('FIM')
