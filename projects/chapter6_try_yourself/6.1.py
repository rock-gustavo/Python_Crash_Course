"""
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and
the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of
information stored in your dictionary.

"""

person = {'first_name': 'clara', 'last_name': 'santos', 'age': 29, 'city': 'brasilia'}

for k, v in person.items():
    print(f'{k} : {v}')
print('FIM')