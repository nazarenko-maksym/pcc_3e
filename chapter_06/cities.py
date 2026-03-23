cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': 3_000_000,
        'fact': 'the best city in the world',
    },
    'boston': {
        'country': 'america',
        'population': 675_647,
        'fact': 'the second best city in the world',
    },
    'sf': {
        'country': 'america',
        'population': 808_000,
        'fact': 'have never been there but looking forward',
    },
}

for city, info in cities.items():
    print(f"{city.title()} information:")
    for k, v in info.items():
        if type(v) == int:
            print(f"\t{k.title()}: {v}")
        else:
            print(f"\t{k.title()}: {v.capitalize()}.")
