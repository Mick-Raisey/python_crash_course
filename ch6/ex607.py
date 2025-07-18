# 6-7. People
user1 = {
    "first_name": "mimi",
    "last_name": "rayzee",
    "age": 13,
    "city": "adelaide",
}

user2 = {
    "first_name": "nugget",
    "last_name": "rayzee",
    "age": 7,
    "city": "adelaide",
}

user3 = {
    "first_name": "john",
    "last_name": "doe",
    "age": 45,
    "city": "melbourne",
}

people = [user1, user2, user3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person["age"]
    city = person["city"]

    print(f"{full_name.title()} from {city.title()} is {age} years old")
