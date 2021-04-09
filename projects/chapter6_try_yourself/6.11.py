"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a
dictionary of information about each city and include the country that the city is in, its approximate population, and
one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact.
Print the name of each city and all of the information you have stored about it.

"""

cities = {
    'brasilia':
        {'country': 'Brazil', 'population': 2_000_000, 'fact': 'Brasilia was founded in 1960.'},
    'são paulo':
        {'country': 'Brazil', 'population': 10_000_000, 'fact': 'São Paulo is the major city in Brazil'},
    'berlin':
        {'country': 'Germany', 'population': 3_645_000, 'fact': 'After the WW2 Berlin was divided until 10/9/1989.'}
}

for city, information in cities.items():
    print(f'City: {city.title()}')
    for k, v in information.items():
        print(f'\t{k.title()}: {v}')