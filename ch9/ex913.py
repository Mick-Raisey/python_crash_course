# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a random
# number between 1 and the number of sides the die has. Make a 6-sided die and
# roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die6 = Die()
print(die6.roll_die())

print("\nResults of rolling a 6 sided die 10 times")
results = []
for roll in range(10):
    number = die6.roll_die()
    results.append(number)
print(results)

print("\nResults of rolling a 10 sided die 10 times")
die10 = Die(sides=10)
die10results = []
for roll in range(10):
    number = die10.roll_die()
    die10results.append(number)
print(die10results)

print("\nResults of rolling a 20 sided die 10 times")
die20 = Die(sides=20)
die20results = []
for roll in range(10):
    number = die20.roll_die()
    die20results.append(number)
print(die20results)
