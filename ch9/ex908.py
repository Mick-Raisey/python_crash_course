# 9-8. Privileges:
# Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges


class User:
    """A simple class to model a user"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize first and last names"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a greeting to the user"""
        print(f"\nWelcome, {self.username}!")


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Shows all the privileges of the admin"""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f" - {privilege}")
        else:
            print("You have no privileges")


mick = Admin("mick", "rayzee", "m_rayzee", "mick@home.com", "australia")
mick.describe_user()

mick.privileges.privileges = [
    "can moderate posts",
    "can ban users",
    "can add new users",
]

mick.privileges.show_privileges()
