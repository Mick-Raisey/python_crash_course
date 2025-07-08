# 3-8. Seeing the World (Bands)
bands = ["kiss", "iron maiden", "acdc", "deep purple", "the angels"]

# Print your list in its original order
print("****** Original Order ******")
print(bands)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print("\n****** sorted() Order ******")
print(sorted(bands))

# Show that your list is still in its original order by printing it.
print("\n****** Still in Original Order ******")
print(bands)

# Use reverse() to change the order of your list.
print("\n****** reverse() ******")
bands.reverse()
print(bands)

# Use reverse() to change the order of your list.
print("\n****** reverse() Back to Original Order ******")
bands.reverse()
print(bands)

# Use sort() to change your list so it’s stored in alphabetical order.
print("\n****** sort() Alphabetical Order ******")
bands.sort()
print(bands)

print("\n****** sort() Reverse Alphabetical Order ******")
bands.sort(reverse=True)
print(bands)
