"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it
a glossary. Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys
in your glossary, and store their meanings as values. Print each word and its meaning as neatly formatted output. You
might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning
indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your
output.
"""

programming_words = {
    'print': 'The command "print" will print on the screen the expression that follows it',
    'import': 'The command "import" is used to import a library or a specific function.'
}

for k, v in programming_words.items():
    print(f'Word: {k}')
    print(f'\t{v}')
print('FIM')