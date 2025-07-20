# 7-8. Deli:

sandwich_orders = ["chicken", "ham", "turkey", "egg and lettuce"]
completed_orders = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Preparing {current_sandwich} sandwich")

    completed_orders.append(current_sandwich)


print(f"\nList of completed sandwiches")
for completed_sandwich in completed_orders:
    print(f"Finished making {completed_sandwich} sandwich")
