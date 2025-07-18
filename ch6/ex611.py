# 6-11. Cities

cities = {
    "santiago": {
        "country": "chile",
        "population": 6_310_000,
        "nearby mountains": "andes",
    },
    "talkeetna": {
        "country": "united states",
        "population": 876,
        "nearby mountains": "alaska range",
    },
    "kathmandu": {
        "country": "nepal",
        "population": 975_453,
        "nearby mountains": "himilaya",
    },
}


for city, info in cities.items():
    country = info["country"].title()
    population = info["population"]
    mountain = info["nearby mountains"].title()

    print(f"\n{city.title()} is in {country.title()}")
    print(f"\tIt has about {population} residents")
    print(f"\tNearby mountain: {mountain}")
