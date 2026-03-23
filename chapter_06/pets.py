cat = {
    'kind': 'cat',
    'owner': 'max',
}
dog = {
    'kind': 'dog',
    'owner': 'marie',
}
bird = {
    'kind': 'bird',
    'owner': 'daria',
}

pets = [cat, dog, bird]

for pet in pets:
    print(f"{pet['owner'].title()} is owner of {pet['kind']}.")
