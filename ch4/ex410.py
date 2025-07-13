# 4-10. Slices: Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:

# 1 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

# 2 Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.

# 3 Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list

bands = ["acdc", "kiss", "iron maiden", "deep purple", "black sabbath"]

print("The first three bands in the list are:")
print(bands[:3])

print("\nThree items from the middle of the list are:")
print(bands[1:4])

print("\nThe last three items in the list are:")
print(bands[-3:])
