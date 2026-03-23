favorite_places = {
    'max': ['kyiv', 'boston', 'amsterdam'],
    'daria': ['kyiv', 'boston', 'paris'],
    'marie': ['boston', 'tokio', 'osaka'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
