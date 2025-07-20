# 7-9. No Pastrami:
#  remove all instances of a certain word from the list

sandwich_orders = [
    "pastrami",
    "curried egg",
    "grilled cheese",
    "pastrami",
    "turkey",
    "roast beef",
    "pastrami",
]

finished_sandwiches = []

print("I'm sorry, we are out of pastrami today.\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"Preparing {current} sandwich")
    finished_sandwiches.append(current)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Finished making {sandwich} sandwich")
