# 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nEnter a topping to add to your pizza"
prompt += "\nEnter 'quit' at anytime to exit: "

while True:
    topping = input(prompt).lower()
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza.")
