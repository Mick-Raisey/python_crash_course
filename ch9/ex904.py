# 9-4. Number Served: Start with your program from Exercise 9-1
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and type of food"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the info about the restaurant"""
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for buisiness")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customers_served):
        """Increment the amount of customers served"""
        if customers_served > self.number_served:
            self.number_served += customers_served


restaurant = Restaurant("uncle wong", "chinese")
print(f"Customers served: {restaurant.number_served}")
restaurant.number_served = 100
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(25)
print(restaurant.number_served)
print("\n86 Customers served today")
restaurant.increment_number_served(86)
print(f"Total customers served: {restaurant.number_served}")
