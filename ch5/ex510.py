# 5-10. Checking Usernames

current_users = ["mick", "mimi", "jack", "jacinta", "nugget"]
new_users = ["jasmine", "mImI", "NuGGet", "bj"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user} is already taken!")
    else:
        print(f"The username {new_user} is available")
