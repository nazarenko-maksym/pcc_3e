favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['max', 'willow', 'miko', 'jen']

for person in people:
    if person in favourite_languages:
        print(f"{person.title()}, thank you for respond!")
    else:
        print(f"{person.title()}, please take a poll.")
