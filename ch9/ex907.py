# 9-7. Admin:


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
        self.privileges = []

    def show_privileges(self):
        """Shows all the privileges of the admin"""
        print("\nAdmin Privileges are:")
        for privilege in self.privileges:
            print(f" - {privilege}")


mick = Admin("mick", "rayzee", "m_rayzee", "mick@home.com", "australia")
mick.describe_user()

mick.privileges = ["can delete posts", "can moderate posts", "can ban users"]
mick.show_privileges()
