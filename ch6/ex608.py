# 6-8. Pets

pets = []

pet = {
    "animal type": "dog",
    "name": "archie",
    "owner": "dani",
    "eats": "dog food",
}
pets.append(pet)

pet = {
    "animal type": "cat",
    "name": "mimi",
    "owner": "viv",
    "eats": "cat food",
}
pets.append(pet)

pet = {
    "animal type": "bird",
    "name": "nugget",
    "owner": "viv",
    "eats": "seed",
}
pets.append(pet)

for pet in pets:
    print(f"\nInformation about {pet['name'].title()}")
    for key, value in pet.items():
        print(f" - {key}: {value}")
