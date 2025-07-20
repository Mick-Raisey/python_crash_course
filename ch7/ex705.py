# 7-5. Movie Tickets

prompt = "\nWhat is the age of the movie goer? "
prompt += "\nEnter 'quit' at anytime to exit "

while True:
    age = input(prompt).lower()
    if age == "quit":
        break
    age = int(age)

    if age < 3:
        print("The tickets are free")
    elif age < 13:
        print("Tickets cost $10")
    else:
        print("Tickets cost $15")
