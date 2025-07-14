# 5-6. Stages of Life:
# Write an if-elif-else chain that determines a person’s stage
# of life. Set a value for the variable age, and then:

# 1. If the person is less than 2 years old, print a message that the person is a baby.
# 2. at least 2 years old but less than 4, print a message that the person is a toddler.
# 3. 4 years old but less than 13, print a message that the person is a kid.
# 4. 13 years old but less than 20, the person is a teenager.
# 5. between 20 and 65, the person is an adult.
# 6. 65 or older, print a message that the person is an elder.

age = 21

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")
