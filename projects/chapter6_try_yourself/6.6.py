"""
6-6. Polling: Use the code in favorite_languages.py (page 97). Make a list of people who should take the favorite
languages poll. Include some names that are already in the dictionary and some that are not. Loop through the list of
people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If
they have not yet taken the poll, print a message inviting them to take the poll.

"""


favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
should_take = ['jen', 'sarah', 'clara', 'gustavo']

for c in should_take:
       if c in favorite_languages:
              print(f'\n{c.title()}, thank you for responding the poll!')
       else:
              print(f'\n\t{c.title()} you should take the poll!')
