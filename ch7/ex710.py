# 7-10. Dream Vacation:
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

name_input = "What's your name? "
place = "If you could visit one place in the world, where would you go? "

responses = {}

while True:
    name = input(name_input)
    response = input(place)

    responses[name] = response

    repeat = input("Another response? (y/n) ")

    if repeat == "n" or repeat == "no":
        break

print("\n---------- Results ----------")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}")
