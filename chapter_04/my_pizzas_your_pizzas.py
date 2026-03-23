pizzas = ['margherita', 'salami', 'pepperoni']

friend_pizzas = pizzas[:]

pizzas.append('four cheeses')
friend_pizzas.append('hawaiian')

print(f"My favourite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")

print(f"My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")
