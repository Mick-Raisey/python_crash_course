# 4-8. Cubes:
# Make a list of the first 10 cubes from 1 through 10,
# and use a for loop to print out the value of each cube.

cubes = []
for number in range(1, 11):
    cubes.append(number**3)

for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension:
cubes = [i**3 for i in range(1, 11)]

for cube in cubes:
    print(cube)
