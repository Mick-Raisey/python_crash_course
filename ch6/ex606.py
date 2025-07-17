# 6-6. Polling: Use the code in favorite_languages.py (page 96).

# 1 Make a list of people who should take the favorite languages poll. Include
#   some names that are already in the dictionary and some that are not.
# 2 Loop through the list of people who should take the poll. If they have
#   already taken the poll, print a message thanking them for responding.
#   If they have not yet taken the poll, print a message inviting them to take the poll.

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

invites = ["mimi", "phil", "nugget", "jack", "jen"]

for person in invites:
    if person in favourite_languages.keys():
        print(f"Thanks for taking the poll, {person.title()}")
    else:
        print(f"{person.title()}, please take the favourite languages poll!")
