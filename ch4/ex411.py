# 4-11. My Pizzas
# Your Pizzas/Bands: Start with your program from Exercise 4-1 (page 56).
# Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:

# 1 Add a new pizza/band to the original list.
# 2 Add a different pizza/band to the list friend_pizzas.
# 3
# Prove that you have two separate lists. Print the message My favorite pizzas are:,
# and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

my_bands = ["acdc", "kiss", "iron maiden", "deep purple", "black sabbath"]
friend_bands = my_bands[:]

my_bands.append("green day")
friend_bands.append("led zeppelin")

print("My favourite bands are:")
for band in my_bands:
    print(f" - {band}")

print("\nFriend favourite bands are:")
for band in friend_bands:
    print(f" - {band}")
