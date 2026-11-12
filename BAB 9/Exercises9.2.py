class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

        
restaurant_one = Restaurant("Spice Route", "Indian")
restaurant_two = Restaurant("Sakura", "Japanese")
restaurant_three = Restaurant("Taco Corner", "Mexican")

# Call describe_restaurant() for each instance
restaurant_one.describe_restaurant()
print()
restaurant_two.describe_restaurant()
print()
restaurant_three.describe_restaurant()