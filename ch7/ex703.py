# 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = int(input("Input any number you like: "))

if number % 10 == 0:
    print(f"{number} is indeed a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")
