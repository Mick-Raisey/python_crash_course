# 7-2. Restaurant Seating:
# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight,
# print a message saying they’ll have to wait for a table.
# Otherwise, report that their table is ready.

guests = int(input("How many people are in the group? "))

if guests > 8:
    print("You will have to wait for an available table.")
else:
    print("Your table is ready")
