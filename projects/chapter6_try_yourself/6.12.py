"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of
ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the
context of the program or improving the formatting of the output.

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