# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.


def make_car(manufacturer, model, **extras):
    """Make a dictionary descriving a car"""
    car_dictionary = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }

    for key, value in extras.items():
        car_dictionary[key] = value

    return car_dictionary


mustang = make_car("ford", "mustang", color="orange", sunroof=True)
print(mustang)

chevy = make_car("corvette", "stingray", color="black", year=1969, convertible=True)
print(chevy)
