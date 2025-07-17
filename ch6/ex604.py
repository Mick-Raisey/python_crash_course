# 6-4. Glossary 2:
# Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values.

glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the Python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one at a time.",
    "dictionary": "A collection of key-value pairs.",
    "set": "An unordered collection of unique elements.",
}

for k, v in glossary.items():
    print(k.title())
    print(f" - {v}")
