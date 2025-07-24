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


mickey = User(
    "mickey", "mouse", "mickey_mouse", "mickey_mouse@disneyland.com", "america"
)
mickey.describe_user()
mickey.greet_user()

donald = User("donald", "duck", "donald_duck", "d_duck@disneyland.com", "america")
donald.describe_user()
donald.greet_user()
