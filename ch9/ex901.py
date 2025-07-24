class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and type of food"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the info about the restaurant"""
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for buisiness")


restaurant = Restaurant("cone-on", "ice cream")
restaurant.describe_restaurant()
restaurant.open_restaurant()
