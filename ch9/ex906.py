# 9-6. Ice Cream Stand:


class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the name and type of food"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the info about the restaurant"""
        print(f"{self.name} serves delicious {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open for buisiness")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customers_served):
        """Increment the amount of customers served"""
        if customers_served > self.number_served:
            self.number_served += customers_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type="ice cream"):
        super().__init__(name, cuisine_type)
        self.flavours = []

    def show_flavours(self):
        """Display all the flavours available"""
        print(f"We have the following flavours")
        for flavour in self.flavours:
            print(f" - {flavour}")


cone_on = IceCreamStand("cone-on")
cone_on.flavours = ["chocolate", "vanilla", "strawberry", "bannana"]

cone_on.describe_restaurant()
cone_on.show_flavours()
