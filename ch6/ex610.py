# 6-10. Favorite Numbers

favourite_numbers = {
    "nugget": [13, 6, 21],
    "jacinta": [5, 17],
    "mimi": [32, 3, 7],
}

for person, numbers in favourite_numbers.items():
    print(f"{person.title()}s favourite numbers are:")
    for number in numbers:
        print(f" - {number}")
