def city_country(city, country, population=0):
    if population:
        result = f"{city}, {country}".title() + f" - population {population}"
    else:
        result = f"{city}, {country}".title()
    return result
