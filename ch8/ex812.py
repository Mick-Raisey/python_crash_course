# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.


def sadwiches(*items):
    print("\nYou wanted these items on your sandwich.")
    for item in items:
        print(f" - {item}")


sadwiches("egg", "lettuce", "mayonaise")
sadwiches("roast beef", "cheese")
sadwiches("turkey", "mustard")
