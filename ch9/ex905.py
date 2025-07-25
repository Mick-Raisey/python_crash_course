# 9-5. Login Attempts:


class User:
    """A simple class to model a user"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize first and last names"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a greeting to the user"""
        print(f"\nWelcome, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User(
    "joe",
    "bloggs",
    "joe_bloggs",
    "j_bloggs@home.com",
    "somewhere",
)

print(f"Login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
