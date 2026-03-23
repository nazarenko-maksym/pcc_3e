class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\" has \"{self.cuisine_type}\" cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant_1 = Restaurant("eataly", "italian")
restaurant_2 = Restaurant("veselka", "ukrainian")
restaurant_3 = Restaurant("mcdonalds", "american")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
