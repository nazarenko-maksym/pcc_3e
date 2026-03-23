person_1 = {
    'first_name': 'willow',
    'last_name': 'miko',
    'age': 2,
    'city': 'boston',
}

person_2 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': 50,
    'city': 'princeton',
}

person_3 = {
    'first_name': 'marie',
    'last_name': 'curie',
    'age': 60,
    'city': 'paris',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name.title()} is {age} old living in {city.title()}.")
