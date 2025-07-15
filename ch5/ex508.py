# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user.

# 1. If the username is 'admin', print a special greeting, such as
#    Hello admin, would you like to see a status report?
# 2 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
#   logging in again.

# 5-9. No Users:
# Add an if test to make sure the list of users is not empty.

usernames = ["mick", "admin", "mimi", "jacinta"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello, {username.title()}, thanks for logging in again.")
else:
    print("There are no users in the list")
