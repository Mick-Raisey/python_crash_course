# 4-13. Buffet/Bands:
# A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple.

# 1 Use a for loop to print each food the restaurant offers.

# 2 Try to modify one of the items, and make sure that Python rejects the
# change.

# 3 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

bands = ("iron maiden", "acdc", "the angels", "foo fighters", "the who")

for band in bands:
    print(band.upper())

# this will result in an error
# bands[0] = "midnight oil"

bands = ("inxs", "the rolling stones", "the beatles", "chuck berry")

print("\nThe new bands list is:")
for band in bands:
    print(band.upper())
