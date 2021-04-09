"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite
number. Then print each person’s name along with their favorite numbers.

"""

fav_number = {'gustavo': [11, 7], 'clara': [7, 17], 'enzo': [7, 8]}

for k, v in fav_number.items():
    print(f"{k.title()}'s favorite numbers are: ")
    for c in v:
        print(f'\t{c}')
print('FIM')