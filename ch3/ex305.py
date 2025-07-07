# 3-5. Changing Guest List:
# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

guests = ["bon scott", "ace frehley", "freddie mercury"]

guest = guests[0].title()
print(f"{guest}, you are invited to the jam")

guest = guests[1].title()
print(f"{guest}, you are invited to the jam")

guest = guests[2].title()
print(f"{guest}, you are invited to the jam")

guest = guests[1].title()
print(f"\n{guest} can't make it to the jam")

# Invite Malcolm instead
del guests[1]
guests.insert(1, "malcolm young")

guest = guests[0].title()
print(f"{guest}, you are invited to the jam")

guest = guests[1].title()
print(f"{guest}, you are invited to the jam")

guest = guests[2].title()
print(f"{guest}, you are invited to the jam")
