
# ATENTION!!!
"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list
called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have
been made, print a message listing each sandwich that was made.

"""
sandwich_orders = ['spice', 'cowboy', 'cowgirls', 'yahoo']
finished_sandwiches = []

"""
for sandwich in sandwich_orders:
    print(f"\nWe are now preparing your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich_orders.pop()) 
"""

# Quando o número de itens da lista é reduzido utilizando o "pop()", é reduzido o número de ciclos do "for". Assim, ao
# iniciar o primeiro ciclo, o programa registra 4 ciclos. Ao final do primeiro ciclo, conpleta-se um ciclo e a função
# "pop()" retira mais um elemento. Assim, quando o segundo ciclo inicia, são registrados 2 ciclos. Quando o segundo
# ciclo termina, completa-se mais um ciclo e a função "pop()" retira mais um elemento. Assim, não se inicia o terceiro
# ciclo.

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nWe are now preparing your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

print("\nWe have finished the following sandwiches:")
for c in finished_sandwiches:
    print(f"\t{c}")
