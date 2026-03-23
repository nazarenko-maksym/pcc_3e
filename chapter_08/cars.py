def make_car(manufacturer, model, **kwargs):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for k,v in kwargs.items():
        car[k] = v
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
